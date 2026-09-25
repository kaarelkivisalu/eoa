from sqlalchemy import Select, func, or_, select

from app.models import Contestant

MIN_PARTICIPATIONS = 10


def qualified_student_ids() -> Select[tuple[int | None]] | Select[tuple[int]]:
    """Students eligible for name search and school rosters."""
    return (
        select(Contestant.person_id)
        .group_by(Contestant.person_id)
        .having(
            or_(
                func.count(Contestant.id) >= MIN_PARTICIPATIONS,
                func.sum(Contestant.placement.in_((1, 2, 3))) > 0,
            )
        )
    )
