"""FastAPI application factory and default application instance."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.db import create_db_engine, initialize_database
from app.routes import inspections, yards

APP_DIRECTORY = Path(__file__).resolve().parent


def create_app(database_url: str | None = None) -> FastAPI:
    """Create an application with its own database engine."""
    engine = create_db_engine(database_url)

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        initialize_database(engine)
        yield

    application = FastAPI(
        title="Hof-App",
        description="Manage fictional yards and their inspection history.",
        lifespan=lifespan,
    )
    application.state.engine = engine
    application.include_router(yards.router)
    application.include_router(inspections.router)
    application.mount(
        "/static",
        StaticFiles(directory=APP_DIRECTORY / "static"),
        name="static",
    )
    return application


app = create_app()
