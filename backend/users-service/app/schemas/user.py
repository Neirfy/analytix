from pydantic import BaseModel, ConfigDict
from uuid import UUID


class CreateUserSchema(BaseModel):
    username: str
    email: str | None = None
    phone: str | None = None


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: str | None
    phone: str | None


class UpdateUsernameSchema(BaseModel):
    username: str


class UpdateEmailSchema(BaseModel):
    email: str


class UpdatePhoneSchema(BaseModel):
    phone: str
