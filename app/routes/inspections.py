"""Routes for creating yard inspections."""

from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.db import get_session
from app.models import InspectionResult
from app.services import inspection_service, yard_service

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
SessionDependency = Annotated[Session, Depends(get_session)]


@router.get("/yards/{yard_id}/inspections/new", response_class=HTMLResponse)
def new_inspection_form(
    request: Request,
    yard_id: int,
    session: SessionDependency,
) -> HTMLResponse:
    """Render the form used to record an inspection."""
    yard = yard_service.get_yard(session, yard_id)
    if yard is None:
        raise HTTPException(status_code=404, detail="Yard not found")

    return templates.TemplateResponse(
        request=request,
        name="inspections/create.html",
        context={"yard": yard, "results": list(InspectionResult)},
    )


@router.post("/yards/{yard_id}/inspections")
def create_inspection(
    yard_id: int,
    session: SessionDependency,
    inspection_date: Annotated[date, Form()],
    inspector: Annotated[str, Form(min_length=2, max_length=100)],
    result: Annotated[InspectionResult, Form()],
    comment: Annotated[str, Form(max_length=500)] = "",
) -> RedirectResponse:
    """Validate and persist a new inspection."""
    if yard_service.get_yard(session, yard_id) is None:
        raise HTTPException(status_code=404, detail="Yard not found")

    inspection_service.create_inspection(
        session=session,
        yard_id=yard_id,
        inspection_date=inspection_date,
        inspector=inspector.strip(),
        result=result,
        comment=comment.strip(),
    )
    return RedirectResponse(
        url=f"/yards/{yard_id}",
        status_code=status.HTTP_303_SEE_OTHER,
    )
