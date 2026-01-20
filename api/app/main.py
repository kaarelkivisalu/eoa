from fastapi import FastAPI

from app.routes.subcontest import router as subcontest_router
from app.routes.people import router as people_router
from app.routes.schools import router as schools_router
from app.routes.statistics import router as statistics_router
from app.schemas import HealthResponse

app = FastAPI(title="EOA API")

app.include_router(subcontest_router)
app.include_router(people_router)
app.include_router(schools_router)
app.include_router(statistics_router)


@app.get("/health", response_model=HealthResponse)
def health() -> dict[str, str]:
    return {"status": "ok"}
