from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Executive Coaching Agent",
    description="AI Executive Coaching Platform MVP",
    version="0.1"
)

app.include_router(router)