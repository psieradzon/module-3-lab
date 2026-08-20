"""Tests for database initialization."""

from sqlmodel import Session, select

from app.database.db import initialize_database
from app.models import Inspection, Yard


def test_database_is_seeded_once(session: Session) -> None:
    initialize_database(session.get_bind())

    yards = session.exec(select(Yard)).all()
    inspections = session.exec(select(Inspection)).all()

    assert len(yards) == 3
    assert len(inspections) == 5
