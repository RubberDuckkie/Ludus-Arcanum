import math
from datetime import datetime, timezone

from .config import weights


def genre_affinity(game, genre_hours: dict, total_hours: float) -> float:
    'Calculates the genre affinity score for a game based on the user\'s playtime in that genre.'
    return genre_hours.get(game.genre, 0) / total_hours if total_hours else 0

def recency_decay(game, half_life_days: float = 30) -> float:
    'Calculates the recency decay score for a game based on how recently it was played.'
    days_since = (datetime.now(timezone.utc) - game.last_played).days
    return math.exp(-days_since / half_life_days)

def session_fit(game, available_minutes: int) -> float:
    'Calculates the session fit score for a game based on the available playtime.'
    if game.typical_session_length is None:
        return 0
    return min(1, available_minutes / game.typical_session_length)

def chill_intense_score(game, slider: float) -> float:
    'Calculates the chill/intense score for a game based on the user\'s preference.'
    if game.review_pct is None:
        return 0
    return (game.review_pct - 0.5) * slider

def score_game(game, context) -> float:
    return (
        weights.w_genre * genre_affinity(game, context.genre_hours, context.total_hours)
        + weights.w_recency * recency_decay(game)
        + weights.w_session_fit * session_fit(game, context.available_minutes)
        + weights.w_chill_intense * chill_intense_score(game, context.slider)
    )