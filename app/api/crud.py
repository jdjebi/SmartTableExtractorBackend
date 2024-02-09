from sqlalchemy.orm import Session

from . import models
from . import schemas 

def get_extractor(db: Session, extractor_id: int):
    return db.query(models.Extractor).filter(models.Extractor.id == extractor_id).first()

def get_extractor_by_name(db: Session, extractor_name: str):
    return db.query(models.Extractor).filter(models.Extractor.name == extractor_name).first()

def get_all_extractors(db: Session):
    return db.query(models.Extractor).all()

def create_extractor(db: Session, extractor: schemas.Extractor):
    db_extractor = models.Extractor(**extractor.dict())
    db.add(db_extractor)
    db.commit()
    db.refresh(db_extractor)
    return db_extractor