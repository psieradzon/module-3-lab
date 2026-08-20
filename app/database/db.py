"""Database engine, session dependency, and initialization."""

import os
from collections.abc import Iterator
from pathlib import Path

from fastapi import Request
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine, select

from app.database.seed import load_seed_data
from app.models import Yard

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATABASE_URL = f"sqlite:///{PROJECT_ROOT / 'data' / 'yard_management.db'}"


def create_db_engine(database_url: str | None = None) -> Engine:
    """Create a SQLModel engine for the configured database."""
    url = database_url or os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=connect_args)


def initialize_database(engine: Engine) -> None:
    """Create tables and load seed data when the database is empty."""
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if session.exec(select(Yard)).first() is None:
            load_seed_data(session)


def get_session(request: Request) -> Iterator[Session]:
    """Provide a database session bound to the current application."""
    with Session(request.app.state.engine) as session:
        yield session
