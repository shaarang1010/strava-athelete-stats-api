from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.database import Base


class StravaAthlete(Base):
    __tablename__ = 'atheletes'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    city = Column(String)
    profile = Column(String)
    ftp = Column(Integer, default=153)
    weight = Column(Float)
    is_active = Column(Boolean, default=True)

    stats = relationship("Stats", back_populates="athletes")   
