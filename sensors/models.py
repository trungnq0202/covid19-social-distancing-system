from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Motion(Base):
    __tablename__ = "motion"

    id = Column(Integer, primary_key=True, index=True)
    people = Column(Integer)
    prev = Column(Integer)
    cur = Column(Integer)
    
class Envi(Base):
    __tablename__ = "envi"

    id = Column(Integer, primary_key=True, index=True)
    humi = Column(Integer)
    temp = Column(Integer)
    mois = Column(Integer)
    level = Column(String)
