from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routers.student_routes import router as student_router

from app.models import student

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Student CRUD API", lifespan=lifespan)

app.include_router(student_router)


@app.get("/")
async def root():
    return {"message": "Student CRUD API is running"}
