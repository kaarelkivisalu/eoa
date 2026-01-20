from fastapi import FastAPI

from app.routes.results import router as results_router
from app.routes.subcontests import router as subcontests_router
from app.routes.subjects import router as subjects_router

app = FastAPI(title="EOA API")

app.include_router(results_router)
app.include_router(subcontests_router)
app.include_router(subjects_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
