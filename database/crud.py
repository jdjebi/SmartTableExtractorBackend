from sqlalchemy.orm import Session

from . import models, schemas 

def get_extractor(db: Session, extractor_id: int):
    return db.query(models.Extractor).filter(models.Extractor.id == extractor_id).first()

def get_all_extractors(db: Session):
    return db.query(models.Extractor).all()

def create_extractor(db: Session, extractor: schemas.Extractor):
    db_extractor = models.Extractor(**extractor.model_dump())
    db.add(db_extractor)
    db.commit()
    db.refresh(db_extractor)
    return db_extractor