from typing import Union

from pydantic import BaseModel


class Extractor(BaseModel):
    id: Union[int, None]
    name: str
    description: Union[str, None] = ""