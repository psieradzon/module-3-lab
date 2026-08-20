"""Tests for creating inspections."""

from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.models import Inspection, InspectionResult


def test_new_inspection_form_renders_for_existing_yard(client: TestClient) -> None:
    response = client.get("/yards/1/inspections/new")
    assert response.status_code == 200
    assert "Inspektion erfassen" in response.text
    assert "Nordhof" in response.text


def test_new_inspection_form_returns_404_for_unknown_yard(client: TestClient) -> None:
    response = client.get("/yards/999/inspections/new")
    assert response.status_code == 404


def test_create_inspection_persists_valid_submission(client: TestClient, session: Session) -> None:
    response = client.post(
        "/yards/1/inspections",
        data={
            "inspection_date": "2026-08-12",
            "inspector": "Taylor Kim",
            "result": "issues_found",
            "comment": "Gate latch requires adjustment.",
        },
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/yards/1"

    inspections = session.exec(select(Inspection).where(Inspection.inspector == "Taylor Kim")).all()
    assert len(inspections) == 1
    assert inspections[0].result == InspectionResult.ISSUES_FOUND


def test_create_inspection_rejects_invalid_result(client: TestClient) -> None:
    response = client.post(
        "/yards/1/inspections",
        data={"inspection_date": "2026-08-12", "inspector": "Taylor Kim", "result": "unknown", "comment": "Invalid result value."},
    )
    assert response.status_code == 422


def test_create_inspection_returns_404_for_unknown_yard(client: TestClient) -> None:
    response = client.post(
        "/yards/999/inspections",
        data={"inspection_date": "2026-08-12", "inspector": "Taylor Kim", "result": "passed", "comment": "No issues found."},
    )
    assert response.status_code == 404
