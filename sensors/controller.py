from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# uvicon controller:app --reload
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/motions/add/{people}/{prev}/{cur}", response_model=schemas.Motion)
def create_motion(people: int, prev: float, cur: float, db: Session = Depends(get_db)):
    motion = models.Motion(people=people, prev=prev, cur=cur)
    return service.create_motion(db=db, motion=motion)

@app.post("/envi/add/{humi}/{temp}/{mois}/{level}", response_model=schemas.Envi)
def create_envi(humi: float, temp: float, mois: float, level: str, db: Session = Depends(get_db)):
    envi = models.Envi(humi=humi, temp=temp, mois=mois, level=level)
    return service.create_envi(db=db, envi=envi)

@app.get("/motions/get/all", response_model=List[schemas.Motion])
def read_motions(db: Session = Depends(get_db)):
    motions = service.get_all_motions(db)
    return motions

@app.get("/envi/get/all", response_model=List[schemas.Envi])
def read_envi(db: Session = Depends(get_db)):
    envi = service.get_all_envi(db)
    return envi

@app.delete("/motions/delete/all")
def delete_all_motions(db: Session = Depends(get_db)):
    return service.delete_all_motions(db)

@app.delete("/envi/delete/all")
def delete_all_envi(db: Session = Depends(get_db)):
    return service.delete_all_envi(db)