"""Load fictional yard and inspection data from JSON."""

import json
from datetime import date
from pathlib import Path

from sqlmodel import Session

from app.models import Inspection, InspectionResult, Yard, YardStatus

SEED_FILE = Path(__file__).resolve().parents[2] / "data" / "seed.json"


def load_seed_data(session: Session, seed_file: Path = SEED_FILE) -> None:
    """Insert the repository's fictional sample data."""
    raw_data = json.loads(seed_file.read_text(encoding="utf-8"))

    for yard_data in raw_data["yards"]:
        session.add(
            Yard(
                id=yard_data["id"],
                code=yard_data["code"],
                name=yard_data["name"],
                city=yard_data["city"],
                status=YardStatus(yard_data["status"]),
            )
        )

    for inspection_data in raw_data["inspections"]:
        session.add(
            Inspection(
                id=inspection_data["id"],
                yard_id=inspection_data["yard_id"],
                inspection_date=date.fromisoformat(inspection_data["inspection_date"]),
                inspector=inspection_data["inspector"],
                result=InspectionResult(inspection_data["result"]),
                comment=inspection_data["comment"],
            )
        )

    session.commit()
