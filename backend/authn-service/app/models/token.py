from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, UUID
from core.base import Base


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID, index=True)
    token: Mapped[str] = mapped_column(String, unique=True)
    expires_at: Mapped[datetime]
