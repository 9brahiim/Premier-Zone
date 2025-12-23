from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/v1/player", tags=["players"])


@router.get("", response_model=List[schemas.PlayerOut])
def get_players(
    team: Optional[str] = None,
    name: Optional[str] = None,
    position: Optional[str] = None,
    nation: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = select(models.Player)

    if team:
        query = query.where(models.Player.team == team)
    if name:
        query = query.where(models.Player.name.ilike(f"%{name}%"))
    if position:
        query = query.where(models.Player.pos.ilike(f"%{position}%"))
    if nation:
        query = query.where(models.Player.nation.ilike(f"%{nation}%"))

    return db.execute(query).scalars().all()


@router.post("", response_model=schemas.PlayerOut, status_code=status.HTTP_201_CREATED)
def add_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    existing = db.get(models.Player, player.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Player already exists")

    db_player = models.Player(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


@router.put("/{player_name}", response_model=schemas.PlayerOut)
def update_player(player_name: str, updated: schemas.PlayerUpdate, db: Session = Depends(get_db)):
    db_player = db.get(models.Player, player_name)
    if not db_player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    for field, value in updated.model_dump(exclude_unset=True).items():
        setattr(db_player, field, value)

    db.commit()
    db.refresh(db_player)
    return db_player


@router.delete("/{player_name}", status_code=status.HTTP_200_OK)
def delete_player(player_name: str, db: Session = Depends(get_db)):
    db_player = db.get(models.Player, player_name)
    if not db_player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    db.delete(db_player)
    db.commit()
    return {"detail": "Player deleted successfully"}

