from fastapi import FastAPI
from src.routes import upload
from src.routes import charts


app = FastAPI()

# router
app.include_router(upload.router)
app.include_router(charts.router)