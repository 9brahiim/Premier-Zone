import os
from functools import lru_cache
from typing import List

from pydantic import BaseModel, AnyUrl, Field


class Settings(BaseModel):
    database_url: AnyUrl = Field(default="postgresql://postgres:password@localhost:5432/pl_data")
    allowed_origins: List[str] = Field(default_factory=lambda: [
        "http://localhost:3000",
    ])

    class Config:
        extra = "ignore"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    database_url = os.getenv("DATABASE_URL")
    allowed_origins_env = os.getenv("ALLOWED_ORIGINS")

    allowed_origins = (
        [origin.strip() for origin in allowed_origins_env.split(",") if origin.strip()]
        if allowed_origins_env
        else None
    )

    return Settings(
        database_url=database_url or Settings.__fields__["database_url"].default,
        allowed_origins=allowed_origins or Settings.__fields__["allowed_origins"].default,
    )

