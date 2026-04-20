from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    JWKS_URL: str

    AUTHN_SERVICE_URL: str
    AUTHZ_SERVICE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()  # pyright: ignore
