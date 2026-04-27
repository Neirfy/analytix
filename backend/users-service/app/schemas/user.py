from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str


class UserSchema(BaseModel):
    username: str


class UpdateUserSchema(BaseModel):
    username: str
