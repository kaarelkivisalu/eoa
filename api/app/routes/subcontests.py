from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.db import get_session
from app.models import Contest, Subcontest

router = APIRouter(tags=["subcontests"])


@router.get("/subcontest-ids")
def list_subcontest_ids(*, session: Session = Depends(get_session)) -> list[dict[str, Any]]:
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
    for subcontest in subcontests:
        contest = subcontest.contest
        year = contest.year
        out.append(
            {
                "subcontest_id": subcontest.id,
                "contest_name": contest.name,
                "contest_name_display": contest_display_name(subcontest),
                "subcontest": subcontest.name,
                "year": year,
                "season": f"{year}/{year + 1}" if year is not None else None,
                "subject": maybe_name(contest.subject),
                "type": maybe_name(contest.type),
                "age_group": maybe_name(subcontest.age_group),
                "description": subcontest.description,
            }
        )

    return out
