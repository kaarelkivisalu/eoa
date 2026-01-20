from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.domain.subjects import SUBJECT_ABBREV
from app.models import Subject

router = APIRouter(tags=["subjects"])

@router.get("/subjects")
def list_subjects(
    *,
    session: Session = Depends(get_session),
) -> list[dict[str, str]]:
    subjects = session.execute(select(Subject).order_by(Subject.name)).scalars().all()
    out: list[dict[str, str]] = []

    missing: list[str] = []
    for subject in subjects:
        name = subject.name
        abbrev = SUBJECT_ABBREV.get(name)
        if abbrev is None:
            missing.append(name)
            continue

        out.append({"abbrev": abbrev, "name": name})

    if missing:
        missing_sorted = ", ".join(sorted(missing))
        raise HTTPException(
            status_code=500,
            detail=f"Missing hardcoded abbreviations for subjects: {missing_sorted}",
        )

    return out
