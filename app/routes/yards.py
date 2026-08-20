"""Routes for yard overview and detail pages."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.db import get_session
from app.services import inspection_service, yard_service

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
SessionDependency = Annotated[Session, Depends(get_session)]


@router.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    """Redirect visitors to the yard overview."""
    return RedirectResponse(url="/yards", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/yards", response_class=HTMLResponse)
def yard_list(request: Request, session: SessionDependency) -> HTMLResponse:
    """Render all yards."""
    return templates.TemplateResponse(
        request=request,
        name="yards/list.html",
        context={"yards": yard_service.list_yards(session)},
    )


@router.get("/yards/{yard_id}", response_class=HTMLResponse)
def yard_detail(
    request: Request,
    yard_id: int,
    session: SessionDependency,
) -> HTMLResponse:
    """Render a yard and its inspection history."""
    yard = yard_service.get_yard(session, yard_id)
    if yard is None:
        raise HTTPException(status_code=404, detail="Yard not found")

    return templates.TemplateResponse(
        request=request,
        name="yards/detail.html",
        context={
            "yard": yard,
            "inspections": inspection_service.list_inspections(session, yard_id),
        },
    )
