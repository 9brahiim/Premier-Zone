from sqlalchemy import Column, Integer, String, Float

from .database import Base


class Player(Base):
    __tablename__ = "player_stats"

    name = Column(String, primary_key=True, index=True)
    nation = Column(String, nullable=True)
    pos = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    mp = Column(Integer, nullable=True)
    starts = Column(Integer, nullable=True)
    min = Column(Float, nullable=True)
    gls = Column(Float, nullable=True)
    ast = Column(Float, nullable=True)
    pk = Column(Float, nullable=True)
    crdy = Column(Float, nullable=True)
    crdr = Column(Float, nullable=True)
    xg = Column(Float, nullable=True)
    xag = Column(Float, nullable=True)
    team = Column(String, nullable=True)

