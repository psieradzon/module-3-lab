"""Queries and commands for inspection data."""

from datetime import date

from sqlmodel import Session, select

from app.models import Inspection, InspectionResult


def list_inspections(session: Session, yard_id: int) -> list[Inspection]:
    """Return recorded inspections for one yard, newest first."""
    statement = (
        select(Inspection)
        .where(
            Inspection.yard_id == yard_id,
            Inspection.result == InspectionResult.ISSUES_FOUND,
        )
        .order_by(Inspection.inspection_date.desc())
    )
    return list(session.exec(statement).all())


def create_inspection(
    session: Session,
    yard_id: int,
    inspection_date: date,
    inspector: str,
    result: InspectionResult,
    comment: str,
) -> Inspection:
    """Persist and return a new inspection."""
    inspection = Inspection(
        yard_id=yard_id,
        inspection_date=inspection_date,
        inspector=inspector,
        result=result,
        comment=comment,
    )
    session.add(inspection)
    session.commit()
    session.refresh(inspection)
    return inspection
