from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base

class Extractor(Base):
    __tablename__ = "extractors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
