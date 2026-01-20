from fastapi import FastAPI

from app.routes.subcontest import router as subcontest_router
from app.routes.people import router as people_router

app = FastAPI(title="EOA API")

app.include_router(subcontest_router)
app.include_router(people_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
