from __future__ import annotations

from pydantic import Field

from .common import APIModel


class SubjectListItem(APIModel):
    subject_abbrev: str = Field(description="Subject abbreviation (e.g. efo).")
    subject: str = Field(description="Full subject name.")


class ResultsRow(APIModel):
    placement: int | None
    person_name: str | None
    age_group: str | None
    school: str | None
    mentors: list[str]
    fields: list[str]


class ResultsPayload(APIModel):
    title: str
    contest_name: str
    subcontest: str | None
    age_group: str | None
    contest: str | None
    year: int | None
    subject: str | None
    type: str | None
    columns: list[str]
    rows: list[ResultsRow]
