
from fastapi import FastAPI

from api.models.extractor import Extractor
from database.database import SessionLocal, engine
from database import crud, models, schemas

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

@app.post("/api/extractors")
def create_extractor(extractor: schemas.Extractor):
    extractor.id = 1
    return extractor