from datetime import datetime

from pydantic import BaseModel


class Game(BaseModel):
    'Sets up the Game model for the database'
    appid: int
    name: str
    genre: str
    playtime_forever: int         
    last_played: datetime          
    review_pct: float | None = None
    typical_session_length: float | None = None