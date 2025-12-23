from typing import Optional

from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    nation: Optional[str] = None
    pos: Optional[str] = None
    age: Optional[int] = None
    mp: Optional[int] = None
    starts: Optional[int] = None
    min: Optional[float] = None
    gls: Optional[float] = None
    ast: Optional[float] = None
    pk: Optional[float] = None
    crdy: Optional[float] = None
    crdr: Optional[float] = None
    xg: Optional[float] = None
    xag: Optional[float] = None
    team: Optional[str] = None


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(BaseModel):
    nation: Optional[str] = None
    pos: Optional[str] = None
    age: Optional[int] = None
    mp: Optional[int] = None
    starts: Optional[int] = None
    min: Optional[float] = None
    gls: Optional[float] = None
    ast: Optional[float] = None
    pk: Optional[float] = None
    crdy: Optional[float] = None
    crdr: Optional[float] = None
    xg: Optional[float] = None
    xag: Optional[float] = None
    team: Optional[str] = None


class PlayerOut(PlayerBase):
    class Config:
        from_attributes = True

