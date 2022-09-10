from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.database import Base

class Stats(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True, index=True)




'''
  "average_speed" : 6.679,
  "max_speed" : 18.5,
  "average_cadence" : 78.5,
  "average_temp" : 4,
  "average_watts" : 185.5,
  "weighted_average_watts" : 230,
  "kilojoules" : 780.5,
  "device_watts" : true,
  "has_heartrate" : false,
  "max_watts" : 743,
  "elev_high" : 446.6,
  "elev_low" : 17.2,
'''