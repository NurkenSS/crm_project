from fastapi import FastAPI
from app.routers import habit

app = FastAPI()

app.include_router(habit.router)
