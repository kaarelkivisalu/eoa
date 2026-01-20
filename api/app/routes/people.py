from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.domain.subjects import SUBJECT_ABBREV
from app.models import AgeGroup, Contest, Contestant, Person, Subject, Subcontest, Type, t_mentor

router = APIRouter(tags=["people"])

@router.get("/people/search")
def search_people(
    *,
    q: str = Query(..., min_length=1, description="Substring search in person name."),
    limit: int = Query(20, ge=1, le=200),
    session: Session = Depends(get_session),
) -> list[dict[str, Any]]:
    query = q.strip()
    if not query:
        raise HTTPException(status_code=422, detail="Query must not be empty")

    rows = session.execute(
        select(Person.id, Person.name)
        .where(Person.publishable == 1)
        .where(Person.name.like(f"%{query}%"))
        .order_by(Person.name)
        .limit(limit)
    ).all()

    return [{"person_id": r.id, "person_name": r.name} for r in rows]


def _season(year: int | None) -> str | None:
    if year is None:
        return None
    return f"{year}-{year + 1}"


def _subject_abbrev(subject_name: str | None) -> str | None:
    if subject_name is None:
        return None
    return SUBJECT_ABBREV.get(subject_name)


@router.get("/contestant/{person_id}")
def contestant(
    *,
    person_id: int = Path(..., gt=0, description="Person ID (must be publishable)."),
    session: Session = Depends(get_session),
) -> list[dict[str, Any]]:
    person_row = session.execute(
        select(Person.name, Person.publishable).where(Person.id == person_id)
    ).one_or_none()
    if person_row is None or person_row.publishable != 1:
        raise HTTPException(status_code=404, detail="Not found")
    person_name: str = person_row.name

    rows = session.execute(
        select(
            Subject.name.label("subject_name"),
            Type.name.label("type_name"),
            Contest.year.label("year"),
            AgeGroup.name.label("age_group"),
            Contestant.placement.label("placement"),
            Contestant.subcontest_id.label("subcontest_id"),
        )
        .select_from(Contestant)
        .join(Person, Contestant.person_id == Person.id)
        .join(Subcontest, Contestant.subcontest_id == Subcontest.id)
        .join(Contest, Subcontest.contest_id == Contest.id)
        .join(Subject, Contest.subject_id == Subject.id, isouter=True)
        .join(Type, Contest.type_id == Type.id, isouter=True)
        .join(AgeGroup, Contestant.age_group_id == AgeGroup.id, isouter=True)
        .where(Contestant.person_id == person_id)
        .where(Person.publishable == 1)
        .order_by(Contest.year.is_(None), Contest.year.desc(), Type.name, AgeGroup.name)
    ).all()

    out: list[dict[str, Any]] = []
    missing: set[str] = set()
    for r in rows:
        subj_abbrev = _subject_abbrev(r.subject_name)
        if r.subject_name is not None and subj_abbrev is None:
            missing.add(r.subject_name)
        out.append(
            {
                "person_name": person_name,
                "subject": subj_abbrev,
                "type": (r.type_name or "").lower() if r.type_name else None,
                "season": _season(r.year),
                "age_group": r.age_group,
                "placement": r.placement,
                "subcontest_id": r.subcontest_id,
            }
        )

    if missing:
        raise HTTPException(
            status_code=500,
            detail=f"Missing hardcoded abbreviations for subjects: {', '.join(sorted(missing))}",
        )

    return out


@router.get("/mentor/{mentor_id}")
def mentor(
    *,
    mentor_id: int = Path(..., gt=0, description="Mentor person ID (must be publishable)."),
    session: Session = Depends(get_session),
) -> list[dict[str, Any]]:
    mentor_row = session.execute(
        select(Person.name, Person.publishable).where(Person.id == mentor_id)
    ).one_or_none()
    if mentor_row is None or mentor_row.publishable != 1:
        raise HTTPException(status_code=404, detail="Not found")
    mentor_name: str = mentor_row.name

    # Only include students that are publishable too.
    student = Person.__table__.alias("student")
    mentor_person = Person.__table__.alias("mentor_person")

    rows = session.execute(
        select(
            student.c.name.label("student_name"),
            Subject.name.label("subject_name"),
            Type.name.label("type_name"),
            Contest.year.label("year"),
            AgeGroup.name.label("age_group"),
            Contestant.placement.label("placement"),
            Contestant.subcontest_id.label("subcontest_id"),
        )
        .select_from(t_mentor)
        .join(Contestant, t_mentor.c.contestant_id == Contestant.id)
        .join(student, Contestant.person_id == student.c.id)
        .join(Subcontest, Contestant.subcontest_id == Subcontest.id)
        .join(Contest, Subcontest.contest_id == Contest.id)
        .join(Subject, Contest.subject_id == Subject.id, isouter=True)
        .join(Type, Contest.type_id == Type.id, isouter=True)
        .join(AgeGroup, Contestant.age_group_id == AgeGroup.id, isouter=True)
        .join(mentor_person, t_mentor.c.mentor_id == mentor_person.c.id)
        .where(t_mentor.c.mentor_id == mentor_id)
        .where(student.c.publishable == 1)
        .where(mentor_person.c.publishable == 1)
        .order_by(Contest.year.is_(None), Contest.year.desc(), Type.name, AgeGroup.name)
    ).all()

    out: list[dict[str, Any]] = []
    missing: set[str] = set()
    for r in rows:
        subj_abbrev = _subject_abbrev(r.subject_name)
        if r.subject_name is not None and subj_abbrev is None:
            missing.add(r.subject_name)
        out.append(
            {
                "mentor_name": mentor_name,
                "student_name": r.student_name,
                "subject": subj_abbrev,
                "type": (r.type_name or "").lower() if r.type_name else None,
                "season": _season(r.year),
                "age_group": r.age_group,
                "placement": r.placement,
                "subcontest_id": r.subcontest_id,
            }
        )

    if missing:
        raise HTTPException(
            status_code=500,
            detail=f"Missing hardcoded abbreviations for subjects: {', '.join(sorted(missing))}",
        )

    return out
