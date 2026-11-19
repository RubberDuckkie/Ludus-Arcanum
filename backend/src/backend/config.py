from pydantic_settings import BaseSettings, SettingsConfigDict

class ScoringWeights(BaseSettings):
    """Scoring weights for different metrics."""

    w_genre: float = 0.35
    w_recency: float = 0.25
    w_session_fit: float = 0.20
    w_chill_intense: float = 0.20

    model_config = SettingsConfigDict(env_file=".env", env_prefix="")

weights = ScoringWeights()


class SteamSettings(BaseSettings):
    steam_api_key: str
    
    model_config = SettingsConfigDict(env_file=".env", env_prefix="")
