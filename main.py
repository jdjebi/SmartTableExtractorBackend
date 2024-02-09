
from typing import Annotated
from fastapi import Body, Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from database.database import engine
from database import crud, models, schemas
from database.session import get_db

# TO DO : Utilise Alembic intégrer un système de migration
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/extractors")
def get_extractors():
    return []

@app.get("/api/extractors/{id}")
def get_extractor(id: int):
    return {
        "id": id
    }

@app.post("/api/extractors", response_model=schemas.Extractor)
def create_extractor(new_extractor: schemas.Extractor = Body(), 
                     force_create_if_exist : bool = Query(default=False), 
                     db: Session = Depends(get_db)
                    ):

    if force_create_if_exist:
        extractor = crud.get_extractor_by_name(db, new_extractor.name)
        if extractor:
            raise HTTPException(status_code=400, detail="Nom de l'extracteur déjà utilisé.")

    return crud.create_extractor(db, new_extractor)