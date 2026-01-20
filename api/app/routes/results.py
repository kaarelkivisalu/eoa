from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.db import get_session
from app.models import Contest, Contestant, ContestantField, Subcontest, SubcontestColumn

router = APIRouter(tags=["results"])


def _contest_display_name(subcontest: Subcontest) -> str:
    contest = subcontest.contest
    contest_name = contest.name or ""
    year = contest.year
    if year is not None and str(year) not in contest_name:
        contest_name = f"{contest_name} ({year}/{year + 1})".strip()
    return contest_name


@router.get("/subcontests/{subcontest_id}/results")
def get_subcontest_results(
    *,
    subcontest_id: int,
    session: Session = Depends(get_session),
):
    return _get_subcontest_results(
        subcontest_id=subcontest_id,
        session=session,
    )


def _get_subcontest_results(
    *,
    subcontest_id: int,
    session: Session,
):
    subcontest = session.execute(
        select(Subcontest)
        .where(Subcontest.id == subcontest_id)
        .options(
            joinedload(Subcontest.contest).joinedload(Contest.subject),
            joinedload(Subcontest.contest).joinedload(Contest.type),
            joinedload(Subcontest.age_group),
        )
    ).scalar_one_or_none()

    if subcontest is None:
        raise HTTPException(status_code=404, detail="Subcontest not found")

    columns = (
        session.execute(
            select(SubcontestColumn)
            .where(SubcontestColumn.subcontest_id == subcontest_id)
            .order_by(SubcontestColumn.seq_no, SubcontestColumn.id)
        )
        .scalars()
        .all()
    )
    task_ids = [c.id for c in columns]

    contestants = (
        session.execute(
            select(Contestant)
            .where(Contestant.subcontest_id == subcontest_id)
            .options(
                joinedload(Contestant.person),
                joinedload(Contestant.age_group),
                joinedload(Contestant.school),
                joinedload(Contestant.mentor),
            )
            .order_by(Contestant.placement.is_(None), Contestant.placement, Contestant.id)
        )
        .unique()
        .scalars()
        .all()
    )

    entries_by_task_and_contestant: dict[int, dict[int, str]] = {tid: {} for tid in task_ids}
    if task_ids:
        rows = session.execute(
            select(ContestantField.task_id, ContestantField.contestant_id, ContestantField.entry).where(
                ContestantField.task_id.in_(task_ids)
            )
        ).all()
        for task_id, contestant_id, entry in rows:
            entries_by_task_and_contestant.setdefault(task_id, {})[contestant_id] = entry

    contest_name = _contest_display_name(subcontest)
    title = ""
    contest = subcontest.contest
    if contest.subject is not None and contest.type is not None and contest.year is not None:
        title = (
            f"{contest.subject.name} {contest.type.name.lower()} "
            f"{contest.year}/{contest.year + 1} - {subcontest.age_group.name}"
        )

    def maybe_name(value: Any) -> str | None:
        if value is None:
            return None
        name = getattr(value, "name", None)
        return name if isinstance(name, str) else None

    return {
        "title": title,
        "contest_name": contest_name,
        "subcontest": subcontest.name,
        "age_group": subcontest.age_group.name,
        "contest": contest.name,
        "year": contest.year,
        "subject": maybe_name(contest.subject),
        "type": maybe_name(contest.type),
        "columns": [c.name for c in columns],
        "rows": [
            {
                "placement": c.placement,
                "person_name": maybe_name(c.person),
                "age_group": maybe_name(c.age_group),
                "school": maybe_name(c.school),
                "mentors": [
                    name
                    for name in (
                        maybe_name(m) for m in sorted(c.mentor, key=lambda p: p.name)
                    )
                    if name is not None
                ],
                "fields": [entries_by_task_and_contestant.get(col.id, {}).get(c.id, "") for col in columns],
            }
            for c in contestants
        ],
    }
