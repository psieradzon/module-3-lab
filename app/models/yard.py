"""Yard database model."""

from enum import StrEnum

from sqlmodel import Field, SQLModel


class YardStatus(StrEnum):
    """Operational state of a yard."""

    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    INACTIVE = "inactive"


class Yard(SQLModel, table=True):
    """A fictional operational yard."""

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True, max_length=20)
    name: str = Field(max_length=100)
    city: str = Field(max_length=100)
    status: YardStatus = Field(index=True)
