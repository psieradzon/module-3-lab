"""Shared fixtures for route and service tests."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.main import create_app


@pytest.fixture
def client(tmp_path: Path) -> Iterator[TestClient]:
    database_url = f"sqlite:///{tmp_path / 'test.db'}"
    with TestClient(create_app(database_url)) as test_client:
        yield test_client


@pytest.fixture
def session(client: TestClient) -> Iterator[Session]:
    with Session(client.app.state.engine) as database_session:
        yield database_session
