from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Contestant, Person, School, t_mentor

router = APIRouter(tags=["schools"])


@router.get("/school-ids")
def list_school_ids(*, session: Session = Depends(get_session)) -> list[dict[str, Any]]:
    rows = session.execute(select(School.id, School.name).order_by(School.id)).all()
    return [{"school_id": r.id, "school_name": r.name} for r in rows]


def _get_school_or_404(*, school_id: int, session: Session) -> School:
    school = session.execute(select(School).where(School.id == school_id)).scalar_one_or_none()
    if school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@router.get("/schools/{school_id}/students")
def school_students(
    *,
    school_id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
) -> dict[str, Any]:
    school = _get_school_or_404(school_id=school_id, session=session)

    rows = session.execute(
        select(
            Person.id.label("person_id"),
            Person.name.label("person_name"),
            func.count().label("participations"),
        )
        .select_from(Contestant)
        .join(Person, Contestant.person_id == Person.id)
        .where(Contestant.school_id == school_id)
        .where(Person.publishable == 1)
        .group_by(Person.id, Person.name)
        .order_by(func.count().desc(), Person.name)
    ).all()

    return {
        "school_id": school.id,
        "school_name": school.name,
        "students": [
            {
                "person_id": r.person_id,
                "person_name": r.person_name,
                "participations": int(r.participations),
            }
            for r in rows
        ],
    }


@router.get("/schools/{school_id}/mentors")
def school_mentors(
    *,
    school_id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
) -> dict[str, Any]:
    school = _get_school_or_404(school_id=school_id, session=session)

    student = Person.__table__.alias("student")
    mentor_person = Person.__table__.alias("mentor_person")

    rows = session.execute(
        select(
            mentor_person.c.id.label("mentor_id"),
            mentor_person.c.name.label("mentor_name"),
            func.count().label("participations"),
        )
        .select_from(t_mentor)
        .join(Contestant, t_mentor.c.contestant_id == Contestant.id)
        .join(student, Contestant.person_id == student.c.id)
        .join(mentor_person, t_mentor.c.mentor_id == mentor_person.c.id)
        .where(Contestant.school_id == school_id)
        .where(student.c.publishable == 1)
        .where(mentor_person.c.publishable == 1)
        .group_by(mentor_person.c.id, mentor_person.c.name)
        .order_by(func.count().desc(), mentor_person.c.name)
    ).all()

    return {
        "school_id": school.id,
        "school_name": school.name,
        "mentors": [
            {
                "person_id": r.mentor_id,
                "person_name": r.mentor_name,
                "participations": int(r.participations),
            }
            for r in rows
        ],
    }
