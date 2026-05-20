from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.app.api.v1.endpoints import pipeline_router
from backend.app.core.config import settings
from backend.app.database.session import engine, Base
# Ensure all models are imported so they are registered with Base.metadata
from backend.app.models.models import Pipeline, Failure, Fix, Validation

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Automatically create database tables if they do not exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Routers
app.include_router(pipeline_router.router, prefix=f"{settings.API_V1_STR}/pipeline", tags=["pipeline"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Agentic Self-Healing CICD Backend"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

