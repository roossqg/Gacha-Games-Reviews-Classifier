from pydantic import BaseModel


class Gacha_Report(BaseModel):

    game: str
    resume: str
    history: str
    gameplay: str
    characters: str
    events: str
    design: str
    gacha: str
    