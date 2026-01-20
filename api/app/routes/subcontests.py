from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Subcontest

router = APIRouter(tags=["subcontests"])


@router.get("/subcontest-ids")
def list_subcontest_ids(*, session: Session = Depends(get_session)) -> list[int]:
    return session.execute(select(Subcontest.id).order_by(Subcontest.id)).scalars().all()

