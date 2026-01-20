from fastapi import FastAPI

from app.routes.results import router as results_router

app = FastAPI(title="EOA API")

app.include_router(results_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
