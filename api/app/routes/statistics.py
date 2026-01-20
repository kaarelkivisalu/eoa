from __future__ import annotations

import csv
import io
from enum import Enum
from typing import Any

from fastapi import APIRouter, Depends, Query
from fastapi.responses import Response
from sqlalchemy import case, func, or_, select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import AgeGroup, Contestant, Person, Subcontest

router = APIRouter(tags=["statistics"])


class StatisticsFormat(str, Enum):
    json = "json"
    csv = "csv"


def _weight_expr():
    diff = AgeGroup.max_class - AgeGroup.min_class
    return func.least(3, func.greatest(1, func.coalesce(diff, 1)))


@router.get("/statistics/students", response_model=None)
def student_statistics(
    *,
    weighted: bool = Query(
        False,
        description=(
            "If true, 1st/2nd/3rd place sums are weighted by "
            "clamp(age_group.max_class - age_group.min_class, 1, 3)."
        ),
    ),
    format: StatisticsFormat = Query(StatisticsFormat.json),
    session: Session = Depends(get_session),
) -> Any:
    place_value = _weight_expr() if weighted else 1

    total_participations = func.count().label("total_participations")
    first_places = func.sum(case((Contestant.placement == 1, place_value), else_=0)).label(
        "first_places"
    )
    second_places = func.sum(
        case((Contestant.placement == 2, place_value), else_=0)
    ).label("second_places")
    third_places = func.sum(case((Contestant.placement == 3, place_value), else_=0)).label(
        "third_places"
    )

    rows = session.execute(
        select(
            Person.id.label("person_id"),
            Person.name.label("person_name"),
            total_participations,
            first_places,
            second_places,
            third_places,
        )
        .select_from(Contestant)
        .join(Person, Contestant.person_id == Person.id)
        .join(Subcontest, Contestant.subcontest_id == Subcontest.id)
        .join(AgeGroup, Subcontest.age_group_id == AgeGroup.id)
        .where(Person.publishable == 1)
        .group_by(Person.id, Person.name)
        .having(
            or_(
                total_participations >= 10,
                (first_places + second_places + third_places) > 0,
            )
        )
        .order_by(
            total_participations.desc(),
            first_places.desc(),
            second_places.desc(),
            third_places.desc(),
            Person.name,
        )
    ).all()

    fields = [
        "person_id",
        "person_name",
        "total_participations",
        "first_places",
        "second_places",
        "third_places",
    ]
    payload_rows = [
        [
            r.person_id,
            r.person_name,
            int(r.total_participations),
            int(r.first_places or 0),
            int(r.second_places or 0),
            int(r.third_places or 0),
        ]
        for r in rows
    ]

    if format == StatisticsFormat.json:
        return {"fields": fields, "rows": payload_rows}

    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(fields)
    writer.writerows(payload_rows)

    suffix = "_weighted" if weighted else ""
    return Response(
        content=buf.getvalue(),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="student_statistics{suffix}.csv"'},
    )
