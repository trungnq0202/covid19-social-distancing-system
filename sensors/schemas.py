from typing import List, Optional

from pydantic import BaseModel


class MotionBase(BaseModel):
    people: int
    prev: float
    cur: float

class MotionCreate(MotionBase):
    pass

class Motion(MotionBase):
    id: int
    class Config:
        orm_mode = True
        
class EnviBase(BaseModel):
    humi: float
    temp: float
    mois: float
    level: str

class EnviCreate(EnviBase):
    pass

class Envi(EnviBase):
    id: int
    class Config:
        orm_mode = True