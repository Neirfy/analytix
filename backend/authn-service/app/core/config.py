from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    REDIS_PORT: int
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

    # @property
    # def redis_url(self, db: int = 0) -> URL:
    #     return URL.build(
    #         scheme="redis",
    #         host="wave_redis",
    #         port=self.REDIS_PORT,
    #         password=self.REDIS_PASSWORD,
    #         path=f"/{db}",
    #     )


settings = Settings()  # pyright: ignore
