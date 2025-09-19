from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .config.environment import AppEnv

from src.routes import charts
app = FastAPI(title="AI Charts API")

# CORS
origins = AppEnv.allowed_origins.split(' ')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(charts.router)


@app.get("/")
async def root():
    return {
        "message": "Bienvenido a AI Charts API!",
        "routes": [
            "/charts/generate",
            "/charts/build"
        ]
    }
