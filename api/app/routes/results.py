from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
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


@router.get("/results")
def get_results_by_query(
    *,
    id: int = Query(..., gt=0, description="Subcontest ID (matches https://eoa.ee/?id=...)"),
    session: Session = Depends(get_session),
):
    return _get_subcontest_results(
        subcontest_id=id,
        session=session,
    )


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

    has_age_group = any(c.age_group is not None for c in contestants)
    has_school = any(c.school_id is not None for c in contestants)
    has_mentor = any(len(c.mentor) > 0 for c in contestants)

    return {
        "title": title,
        "contest_name": contest_name,
        "meta": {
            "has_age_group": has_age_group,
            "has_school": has_school,
            "has_mentor": has_mentor,
        },
        "subcontest": {
            "id": subcontest.id,
            "name": subcontest.name,
            "tasks_link": subcontest.tasks_link,
            "solutions_link": subcontest.solutions_link,
            "description": subcontest.description,
            "age_group": {"id": subcontest.age_group.id, "name": subcontest.age_group.name},
            "contest": {
                "id": contest.id,
                "name": contest.name,
                "year": contest.year,
                "subject": {"id": contest.subject.id, "name": contest.subject.name}
                if contest.subject is not None
                else None,
                "type": {"id": contest.type.id, "name": contest.type.name}
                if contest.type is not None
                else None,
            },
        },
        "columns": [{"id": c.id, "name": c.name} for c in columns],
        "rows": [
            {
                "contestant_id": c.id,
                "placement": c.placement,
                "person": {"id": c.person_id, "name": c.person.name if c.person else None},
                "age_group": {"id": c.age_group_id, "name": c.age_group.name if c.age_group else None},
                "school": {"id": c.school_id, "name": c.school.name if c.school else None},
                "mentors": [{"id": m.id, "name": m.name} for m in sorted(c.mentor, key=lambda p: p.id)],
                "fields": [entries_by_task_and_contestant.get(col.id, {}).get(c.id, "") for col in columns],
                "fields_by_column_id": {
                    str(col.id): entries_by_task_and_contestant.get(col.id, {}).get(c.id, "")
                    for col in columns
                },
            }
            for c in contestants
        ],
    }
