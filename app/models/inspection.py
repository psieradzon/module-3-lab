"""Inspection database model."""

from datetime import date
from enum import StrEnum

from sqlmodel import Field, SQLModel


class InspectionResult(StrEnum):
    """Possible outcomes of an inspection."""

    PASSED = "passed"
    ISSUES_FOUND = "issues_found"


class Inspection(SQLModel, table=True):
    """An inspection performed at a yard."""

    id: int | None = Field(default=None, primary_key=True)
    yard_id: int = Field(foreign_key="yard.id", index=True)
    inspection_date: date = Field(index=True)
    inspector: str = Field(max_length=100)
    result: InspectionResult = Field(index=True)
    comment: str = Field(default="", max_length=500)
