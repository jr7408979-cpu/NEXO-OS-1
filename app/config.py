from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = Field("NEXO OS", validation_alias="NEXO_APP_NAME")
    environment: str = Field("development", validation_alias="NEXO_ENV")
    debug: bool = Field(True, validation_alias="NEXO_DEBUG")

    telegram_bot_token: str = ""
    discord_bot_token: str = ""
    discord_app_id: str = ""
    paypal_client_id: str = ""
    paypal_client_secret: str = ""
    database_url: str = ""
    ai_api_key: str = ""
    nexo_secret: str = ""


settings = Settings()

APP_NAME = settings.app_name
ENVIRONMENT = settings.environment
DEBUG = settings.debug
