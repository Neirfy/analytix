from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, Boolean, String
from core.base import Base


class AuthUser(Base):
    __tablename__ = "auth_users"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    login: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
