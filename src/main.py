from fastapi import FastAPI
from src.routes import charts
app = FastAPI(title="AI Charts API")
app.include_router(charts.router)