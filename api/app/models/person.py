from __future__ import annotations

from sqlalchemy import Index, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Person(Base):
    __tablename__ = "person"
    __table_args__ = (
        Index("idx_person_name", "name"),
        {
            "comment": "Üks inimene - kui otsustab oma andmed kustutada, saab *siit* "
            "nullida\n\n"
            "Juhul kui siia satuvad valesti kirjutatud variandid nimedest, "
            "saab mõjutatud tabelitest person_id vms järgi ühtseks teha\n\n"
            "publishable - kas nime võib välja näidata(!)",
        },
    )

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    publishable: Mapped[int] = mapped_column(
        TINYINT(1), nullable=False, server_default=text("1")
    )

    person_alias: Mapped[list["PersonAlias"]] = relationship(
        "PersonAlias", back_populates="person"
    )
    contestant: Mapped[list["Contestant"]] = relationship(
        "Contestant", back_populates="person"
    )
    contestant_: Mapped[list["Contestant"]] = relationship(
        "Contestant", secondary="mentor", back_populates="mentor"
    )
