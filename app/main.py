
from fastapi import Body, Depends, FastAPI, HTTPException, Path, Query
from sqlalchemy.orm import Session

from app.api import schemas, crud
from app.database import init_db, get_db

# TO DO : Utilise Alembic pour intégrer un système de migration
init_db()

app = FastAPI()

@app.get("/api/extractors", response_model=list[schemas.Extractor])
def get_extractors(db: Session = Depends(get_db)):
    return crud.get_all_extractors(db)

@app.get("/api/extractors/{id}", response_model=schemas.Extractor)
def get_extractor(id: int = Path(), db: Session = Depends(get_db)):

    extractor = crud.get_extractor(db, id)

    if extractor is None:
        raise HTTPException(status_code=404, detail="Extracteur introuvable.")

    return extractor

@app.post("/api/extractors", response_model=schemas.Extractor)
def create_extractor(new_extractor: schemas.Extractor = Body(), 
                     force_create_if_exist : bool = Query(default=False), 
                     db: Session = Depends(get_db)):
    
    if force_create_if_exist:
        extractor = crud.get_extractor_by_name(db, new_extractor.name)
        if extractor:
            raise HTTPException(status_code=400, detail="Nom de l'extracteur déjà utilisé.")

    return crud.create_extractor(db, new_extractor)