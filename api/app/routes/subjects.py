from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Subject

router = APIRouter(tags=["subjects"])


# NOTE: This map is intentionally hardcoded (as requested). If a new subject is added
# to the DB, update this mapping.
SUBJECT_ABBREV: dict[str, str] = {
    "Füüsika": "FYS",
    "Matemaatika": "MAT",
    "Keemia": "KEE",
    "Bioloogia": "BIO",
    "Astronoomia": "AST",
    "Filosoofia": "FIL",
    "Informaatika": "INF",
    "Maateadused": "MTE",
    "Lingvistika": "LIN",
    "Usundiõpetus": "USU",
    "Emakeel": "EMA",
    "Inglise keel": "ING",
    "Saksa keel": "SAK",
    "Vene keel emakeelena": "VEM",
    "Vene keel võõrkeelena": "VVK",
    "Prantsuse keel": "PRA",
    "Geograafia": "GEO",
    "Inimeseõpetus": "INI",
    "Loodusteadused": "LOO",
}


@router.get("/subjects")
def list_subjects(
    *,
    q: str | None = Query(
        None,
        description="Optional filter (case-insensitive) by subject name or abbreviation.",
    ),
    session: Session = Depends(get_session),
) -> list[dict[str, str]]:
    subjects = session.execute(select(Subject).order_by(Subject.name)).scalars().all()

    q_norm = (q or "").strip().lower()
    out: list[dict[str, str]] = []

    missing: list[str] = []
    for subject in subjects:
        name = subject.name
        abbrev = SUBJECT_ABBREV.get(name)
        if abbrev is None:
            missing.append(name)
            continue

        if q_norm:
            if q_norm not in name.lower() and q_norm not in abbrev.lower():
                continue

        out.append({"abbrev": abbrev, "name": name})

    if missing:
        missing_sorted = ", ".join(sorted(missing))
        raise HTTPException(
            status_code=500,
            detail=f"Missing hardcoded abbreviations for subjects: {missing_sorted}",
        )

    return out
