"""Queries for yard data."""

from sqlmodel import Session, select

from app.models import Yard


def list_yards(session: Session) -> list[Yard]:
    """Return every yard ordered by name."""
    return list(session.exec(select(Yard).order_by(Yard.name)).all())


def get_yard(session: Session, yard_id: int) -> Yard | None:
    """Return one yard by its identifier."""
    return session.get(Yard, yard_id)
