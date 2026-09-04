from pydantic import BaseModel


class Gacha_Report(BaseModel):

    game: str
    resume: str
    history: str
    gameplay: str
    events: str
    gacha: str
    