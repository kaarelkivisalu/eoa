from __future__ import annotations

import csv
import io
from typing import TYPE_CHECKING, cast

from app.schemas import ResultsPayload
from app.services.results import get_results_payload, payload_as_csv

from .fakes import FakeResult, FakeSession, ns

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def test_hidden_person_keeps_nameless_result_without_related_identifiers() -> None:
    group = ns(name="6. klass")
    school = ns(name="Kool")
    mentor = ns(id=9, name="Juhendaja", publishable=1)
    contest = ns(
        name="Võistlus",
        year=2025,
        subject=ns(name="Füüsika"),
        type=ns(name="Lõppvoor"),
        start_date=None,
        end_date=None,
    )
    subcontest = ns(
        contest=contest,
        age_group=group,
        name="6. klass",
        tasks_link=None,
        solutions_link=None,
        description=None,
    )
    visible = ns(
        id=1,
        person_id=101,
        person=ns(name="Nähtav", publishable=1),
        age_group=group,
        school_id=8,
        school=school,
        mentor=[mentor],
        placement=1,
    )
    hidden = ns(
        id=2,
        person_id=102,
        person=ns(name="Peidetud", publishable=0),
        age_group=group,
        school_id=8,
        school=school,
        mentor=[mentor],
        placement=2,
    )
    session = FakeSession(
        results=[
            FakeResult(scalar_one_or_none_value=subcontest),
            FakeResult(scalars_list=[ns(id=7, name="Punktid")]),
            FakeResult(scalars_list=[visible, hidden]),
            FakeResult(rows=[(7, 1, "10"), (7, 2, "8")]),
        ]
    )

    payload = ResultsPayload.model_validate(
        get_results_payload(subcontest_id=3, session=cast("Session", session))
    )

    assert len(payload.rows) == 2
    assert payload.rows[0].person_name == "Nähtav"
    assert payload.rows[0].mentor_links[0].person_name == "Juhendaja"
    nameless = payload.rows[1]
    assert nameless.placement == 2
    assert nameless.fields == ["8"]
    assert nameless.person_id is None
    assert nameless.person_name is None
    assert nameless.school_id is None
    assert nameless.school is None
    assert nameless.age_group is None
    assert nameless.mentors == []
    assert nameless.mentor_links == []

    csv_text = bytes(payload_as_csv(subcontest_id=3, payload=payload).body).decode(
        "utf-8"
    )
    assert "Peidetud" not in csv_text
    assert list(csv.reader(io.StringIO(csv_text)))[2] == ["2", "", "", "", "", "8"]
