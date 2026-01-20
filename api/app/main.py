from fastapi import FastAPI

from app.routes.subcontest import router as subcontest_router

app = FastAPI(title="EOA API")

app.include_router(subcontest_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
