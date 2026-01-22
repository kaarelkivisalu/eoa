from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

import pytest

from .fakes import FakeResult, FakeSession, ns

if TYPE_CHECKING:
    from fastapi.testclient import TestClient

SessionOverrideSetter = Callable[[FakeSession], None]


def test_people_search_requires_q(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(FakeSession(results=[]))
    resp = client.get("/people/search")
    assert resp.status_code == 422


def test_people_search_rejects_whitespace_query(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(FakeSession(results=[]))
    resp = client.get("/people/search", params={"q": "   "})
    assert resp.status_code == 422
    assert resp.json()["detail"] == "Query must not be empty"


def test_people_search_pagination_headers_has_more(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(
        FakeSession(
            results=[
                FakeResult(
                    rows=[
                        ns(id=1, name="Alice"),
                        ns(id=2, name="Alicia"),
                        ns(id=3, name="Alina"),
                    ]
                )
            ]
        )
    )
    resp = client.get("/people/search", params={"q": "ali", "offset": 0, "limit": 2})
    assert resp.status_code == 200
    assert resp.headers["X-Result-Limit"] == "2"
    assert resp.headers["X-Result-Offset"] == "0"
    assert resp.headers["X-Result-Has-More"] == "true"
    assert resp.headers["X-Result-Count"] == "2"
    assert resp.headers["X-Result-Next-Offset"] == "2"
    assert resp.json() == [
        {"person_id": 1, "person_name": "Alice"},
        {"person_id": 2, "person_name": "Alicia"},
    ]


def test_people_search_pagination_headers_no_more(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(
        FakeSession(
            results=[FakeResult(rows=[ns(id=10, name="Bob"), ns(id=11, name="Bobby")])]
        )
    )
    resp = client.get("/people/search", params={"q": "bo", "offset": 5, "limit": 10})
    assert resp.status_code == 200
    assert resp.headers["X-Result-Limit"] == "10"
    assert resp.headers["X-Result-Offset"] == "5"
    assert resp.headers["X-Result-Has-More"] == "false"
    assert resp.headers["X-Result-Count"] == "2"
    assert "X-Result-Next-Offset" not in resp.headers


@pytest.mark.parametrize(
    ("row", "expected_status"),
    [
        (None, 404),
        (ns(name="Hidden Person", publishable=0), 404),
    ],
)
def test_contestant_not_found(
    client: TestClient,
    set_session_override: SessionOverrideSetter,
    row: object | None,
    expected_status: int,
) -> None:
    set_session_override(FakeSession(results=[FakeResult(one_or_none_row=row)]))
    resp = client.get("/contestant/123")
    assert resp.status_code == expected_status
    assert resp.json()["detail"] == "Not found"


def test_contestant_success_maps_fields(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(
        FakeSession(
            results=[
                FakeResult(one_or_none_row=ns(name="Alice Example", publishable=1)),
                FakeResult(
                    rows=[
                        ns(
                            subject_name="Füüsika",
                            type_name="Lahtine",
                            year=2023,
                            age_group="12. klass",
                            placement=1,
                            subcontest_id=99,
                        ),
                        ns(
                            subject_name=None,
                            type_name=None,
                            year=None,
                            age_group=None,
                            placement=None,
                            subcontest_id=100,
                        ),
                    ]
                ),
            ]
        )
    )
    resp = client.get("/contestant/1")
    assert resp.status_code == 200
    assert resp.json() == [
        {
            "person_name": "Alice Example",
            "subject": "efo",
            "type": "lahtine",
            "season": "2023-2024",
            "age_group": "12. klass",
            "placement": 1,
            "subcontest_id": 99,
        },
        {
            "person_name": "Alice Example",
            "subject": None,
            "type": None,
            "season": None,
            "age_group": None,
            "placement": None,
            "subcontest_id": 100,
        },
    ]


def test_contestant_missing_subject_abbrev_is_500(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(
        FakeSession(
            results=[
                FakeResult(one_or_none_row=ns(name="Alice", publishable=1)),
                FakeResult(
                    rows=[
                        ns(
                            subject_name="Some New Subject",
                            type_name="Lahtine",
                            year=2023,
                            age_group="12. klass",
                            placement=1,
                            subcontest_id=1,
                        )
                    ]
                ),
            ]
        )
    )
    resp = client.get("/contestant/1")
    assert resp.status_code == 500
    assert "Missing hardcoded abbreviations for subjects:" in resp.json()["detail"]


@pytest.mark.parametrize(
    ("row", "expected_status"),
    [
        (None, 404),
        (ns(name="Hidden Mentor", publishable=0), 404),
    ],
)
def test_mentor_not_found(
    client: TestClient,
    set_session_override: SessionOverrideSetter,
    row: object | None,
    expected_status: int,
) -> None:
    set_session_override(FakeSession(results=[FakeResult(one_or_none_row=row)]))
    resp = client.get("/mentor/123")
    assert resp.status_code == expected_status
    assert resp.json()["detail"] == "Not found"


def test_mentor_success_maps_fields(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(
        FakeSession(
            results=[
                FakeResult(one_or_none_row=ns(name="Mentor Example", publishable=1)),
                FakeResult(
                    rows=[
                        ns(
                            student_name="Student A",
                            subject_name="Matemaatika",
                            type_name="Lõppvoor",
                            year=2022,
                            age_group="11. klass",
                            placement=2,
                            subcontest_id=50,
                        )
                    ]
                ),
            ]
        )
    )
    resp = client.get("/mentor/1")
    assert resp.status_code == 200
    assert resp.json() == [
        {
            "mentor_name": "Mentor Example",
            "student_name": "Student A",
            "subject": "emo",
            "type": "lõppvoor",
            "season": "2022-2023",
            "age_group": "11. klass",
            "placement": 2,
            "subcontest_id": 50,
        }
    ]


def test_mentor_missing_subject_abbrev_is_500(
    client: TestClient, set_session_override: SessionOverrideSetter
) -> None:
    set_session_override(
        FakeSession(
            results=[
                FakeResult(one_or_none_row=ns(name="Mentor", publishable=1)),
                FakeResult(
                    rows=[
                        ns(
                            student_name="Student",
                            subject_name="Some New Subject",
                            type_name="Lahtine",
                            year=2023,
                            age_group="12. klass",
                            placement=1,
                            subcontest_id=1,
                        )
                    ]
                ),
            ]
        )
    )
    resp = client.get("/mentor/1")
    assert resp.status_code == 500
    assert "Missing hardcoded abbreviations for subjects:" in resp.json()["detail"]
