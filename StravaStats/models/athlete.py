from typing import Optional
from pydantic import BaseModel

class StravaAthlete(BaseModel):
    username: str
    firstname: str
    lastname: str
    city: str
    profile: str
    ftp: float
    weight: float


