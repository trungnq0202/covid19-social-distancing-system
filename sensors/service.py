from sqlalchemy.orm import Session
import models, schemas

def create_motion(db: Session, motion: schemas.MotionCreate):
    db_motion = models.Motion(people=motion.people, prev=motion.prev, cur=motion.cur)
    db.add(db_motion)
    db.commit()
    db.refresh(db_motion)
    return db_motion

def create_envi(db: Session, envi: schemas.EnviCreate):
    db_envi = models.Envi(humi=envi.humi, temp=envi.temp, mois=envi.mois, level=envi.level)
    db.add(db_envi)
    db.commit()
    db.refresh(db_envi)
    return db_envi

def get_all_motions(db: Session):
    return db.query(models.Motion).all()

def get_all_envi(db: Session):
    return db.query(models.Envi).all()

def delete_all_motions(db: Session):
    db.query(models.Motion).delete()
    db.commit()
    return "OK"

def delete_all_envi(db: Session):
    db.query(models.Envi).delete()
    db.commit()
    return "OK"