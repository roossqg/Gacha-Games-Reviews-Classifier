from pydantic import BaseModel
from typing import Literal

class Sentiment(BaseModel):
    labels: list[Literal['POSITIVE','NEGATIVE']]