from pydantic import BaseModel

class ExtractorBase(BaseModel):
    name: str 
    description: str | None = ""

class Extractor(ExtractorBase):
    id: int | None
    
    class Config:
        orm_mode = True