#keep in mind imports are case sensitive and Capitalize
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url : str
    model_config = SettingsConfigDict(
        env_file = ".env"
    )

settings = Settings()