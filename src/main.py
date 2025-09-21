from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes import charts

app = FastAPI(title="AI Charts API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:*",
        "http://localhost:5175",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(charts.router)


@app.get("/")
async def root():
    return {
        "message": "Bienvenido a AI Charts API!",
        "routes": ["/charts/generate", "/charts/build"],
    }
