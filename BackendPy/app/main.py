from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .database import Base, engine
from .routers import players

settings = get_settings()

# Create tables on startup (works with existing DB schema)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PremierZone API (Python)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(players.router)


@app.get("/health")
def health():
    return {"status": "ok"}

