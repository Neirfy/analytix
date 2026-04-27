from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    REDIS_PASSWORD: str

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            path=f"/{self.POSTGRES_DB}",
            query={"async_fallback": "true"},
        )

    def redis_url(self, page):
        return f"redis://:{self.REDIS_PASSWORD}@wave_redis:6379/{page}"

    model_config = SettingsConfigDict(
        env_file="../.env",
        extra="ignore",
    )


settings = Settings()  # pyright: ignore
