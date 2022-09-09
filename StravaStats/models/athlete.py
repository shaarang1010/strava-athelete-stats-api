from typing import Optional
from pydantic import BaseModel
from db.database import Base


class StravaAthlete(Base):
    __tablename__ = 'athelete'
    username: str
    firstname: str
    lastname: str
    city: str
    profile: str
    ftp: float
    weight: float
