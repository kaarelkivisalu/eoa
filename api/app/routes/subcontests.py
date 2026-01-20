from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.db import get_session
from app.domain.subjects import SUBJECT_ABBREV
from app.models import Contest, Subcontest

router = APIRouter(tags=["subcontests"])


@router.get("/subcontest-ids")
def list_subcontest_ids(
    *,
    subject_abbrev: str | None = Query(
        None,
        description="Optional filter by subject abbreviation (e.g. efo, eko, eio, ebo, elo, emo).",
    ),
    session: Session = Depends(get_session),
) -> list[dict[str, Any]]:
    def maybe_name(value: Any) -> str | None:
        if value is None:
            return None
        name = getattr(value, "name", None)
        return name if isinstance(name, str) else None

    def contest_display_name(subcontest: Subcontest) -> str:
        contest = subcontest.contest
        contest_name = contest.name or ""
        year = contest.year
        if year is not None and str(year) not in contest_name:
            contest_name = f"{contest_name} ({year}/{year + 1})".strip()
        return contest_name

    def abbrev_for_subject(subject_name: str | None) -> str | None:
        if subject_name is None:
            return None
        return SUBJECT_ABBREV.get(subject_name)

    subject_filter = subject_abbrev.lower().strip() if subject_abbrev is not None else None
    if subject_filter is not None and subject_filter not in set(SUBJECT_ABBREV.values()):
        raise HTTPException(status_code=400, detail="Invalid subject_abbrev")

    subcontests = (
        session.execute(
            select(Subcontest)
            .options(
                joinedload(Subcontest.age_group),
                joinedload(Subcontest.contest).joinedload(Contest.subject),
                joinedload(Subcontest.contest).joinedload(Contest.type),
            )
            .order_by(Subcontest.id)
        )
        .scalars()
        .all()
    )

    out: list[dict[str, Any]] = []
    missing_subject_abbrev: set[str] = set()
    for subcontest in subcontests:
        contest = subcontest.contest
        year = contest.year
        subj_name = maybe_name(contest.subject)
        subj_abbrev = abbrev_for_subject(subj_name)
        if subj_name is not None and subj_abbrev is None:
            missing_subject_abbrev.add(subj_name)

        if subject_filter is not None and subj_abbrev != subject_filter:
            continue

        out.append(
            {
                "subcontest_id": subcontest.id,
                "contest_name": contest.name,
                "contest_name_display": contest_display_name(subcontest),
                "subcontest": subcontest.name,
                "year": year,
                "season": f"{year}/{year + 1}" if year is not None else None,
                "subject": subj_name,
                "subject_abbrev": subj_abbrev,
                "type": maybe_name(contest.type),
                "age_group": maybe_name(subcontest.age_group),
                "description": subcontest.description,
            }
        )

    if missing_subject_abbrev:
        missing_sorted = ", ".join(sorted(missing_subject_abbrev))
        raise HTTPException(
            status_code=500,
            detail=f"Missing hardcoded abbreviations for subjects: {missing_sorted}",
        )

    return out
