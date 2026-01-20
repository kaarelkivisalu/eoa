from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Path, Query, Response
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Contestant, Person, School, t_mentor
from app.schemas import SchoolParticipantsResponse, SchoolSummary

router = APIRouter(tags=["schools"])


@router.get("/schools", response_model=list[SchoolSummary])
def list_schools(*, session: Session = Depends(get_session)) -> list[SchoolSummary]:
    rows = session.execute(select(School.id, School.name).order_by(School.id)).all()
    return [SchoolSummary(school_id=r.id, school_name=r.name) for r in rows]


@router.get("/schools/search", response_model=list[SchoolSummary])
def search_schools(
    *,
    q: str = Query(..., min_length=1, description="Substring search in school name."),
    offset: int = Query(0, ge=0, description="Pagination offset."),
    limit: int = Query(20, ge=1, le=200),
    response: Response,
    session: Session = Depends(get_session),
) -> list[SchoolSummary]:
    query = q.strip()
    if not query:
        raise HTTPException(status_code=422, detail="Query must not be empty")

    rows = session.execute(
        select(School.id, School.name)
        .where(School.name.like(f"%{query}%"))
        .order_by(School.name, School.id)
        .offset(offset)
        .limit(limit + 1)
    ).all()

    has_more = len(rows) > limit
    response.headers["X-Result-Limit"] = str(limit)
    response.headers["X-Result-Offset"] = str(offset)
    response.headers["X-Result-Has-More"] = "true" if has_more else "false"
    response.headers["X-Result-Count"] = str(min(len(rows), limit))
    if has_more:
        response.headers["X-Result-Next-Offset"] = str(offset + limit)

    return [SchoolSummary(school_id=r.id, school_name=r.name) for r in rows[:limit]]


def _get_school_or_404(*, school_id: int, session: Session) -> School:
    school = session.execute(select(School).where(School.id == school_id)).scalar_one_or_none()
    if school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@router.get("/schools/{school_id}/students", response_model=SchoolParticipantsResponse)
def school_students(
    *,
    school_id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
) -> SchoolParticipantsResponse:
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

    return SchoolParticipantsResponse.model_validate(
        {
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
    )


@router.get("/schools/{school_id}/mentors", response_model=SchoolParticipantsResponse)
def school_mentors(
    *,
    school_id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
) -> SchoolParticipantsResponse:
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

    return SchoolParticipantsResponse.model_validate(
        {
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
    )
