from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models.subcontest import Subcontest
    from app.models.subject import Subject
    from app.models.type import Type
    from app.models.year import Year

from sqlalchemy import Date, ForeignKeyConstraint, Index, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Contest(Base):
    __tablename__ = "contest"
    __table_args__ = (
        ForeignKeyConstraint(["subject_id"], ["subject.id"], name="fk_contest_subject"),
        ForeignKeyConstraint(["type_id"], ["type.id"], name="fk_contest_type"),
        ForeignKeyConstraint(["year_id"], ["year.id"], name="fk_contest_year"),
        Index("fk_subject_idx", "subject_id"),
        Index("fk_type_idx", "type_id"),
        Index("fk_year_idx", "year_id"),
        {"comment": "Üks koos toimuv võistlus - nt. füüsika pkv või keemia lahtine"},
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    subject_id: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    type_id: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    year_id: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    name: Mapped[Optional[str]] = mapped_column(String(128))
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    year: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    subject: Mapped[Subject] = relationship("Subject", back_populates="contest")
    type: Mapped[Type] = relationship("Type", back_populates="contest")
    year_: Mapped[Optional[Year]] = relationship("Year", back_populates="contest")
    subcontest: Mapped[list[Subcontest]] = relationship(
        "Subcontest", back_populates="contest"
    )
