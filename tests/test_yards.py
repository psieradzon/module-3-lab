"""Tests for yard pages."""

from fastapi.testclient import TestClient


def test_root_redirects_to_yard_list(client: TestClient) -> None:
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/yards"


def test_yard_list_renders_seeded_yards(client: TestClient) -> None:
    response = client.get("/yards")
    assert response.status_code == 200
    assert "Höfe" in response.text
    assert "Details anzeigen" in response.text
    assert "Nordhof" in response.text
    assert "Uferhof" in response.text
    assert "Zentralhof" in response.text


def test_yard_detail_renders_yard_information(client: TestClient) -> None:
    response = client.get("/yards/1")
    assert response.status_code == 200
    assert "Nordhof" in response.text
    assert "YRD-001" in response.text


def test_unknown_yard_returns_not_found(client: TestClient) -> None:
    response = client.get("/yards/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Yard not found"}
