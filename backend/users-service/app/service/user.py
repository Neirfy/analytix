from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from uuid import UUID

from repositories.user import UserRepository
from schemas.user import CreateUserSchema, UserSchema, UpdateUserSchema


class UserService:
    def __init__(self, db):
        self.db = db
        self.repo = UserRepository()

    async def get_me(
        self,
        user_id: UUID,
    ) -> UserSchema:
        user = await self.repo.get_by_id(self.db, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="user not found")

        return user

    async def create_user(
        self,
        data: CreateUserSchema,
    ) -> UserSchema:
        try:
            return await self.repo.create(self.db, data)

        except IntegrityError as e:
            raise HTTPException(status_code=409, detail="username already exists")

    async def delete_user(
        self,
        user_id: UUID,
    ):
        user = await self.repo.delete(self.db, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="user not found")

        return user

    async def update_username(
        self,
        user_id: UUID,
        data: UpdateUserSchema,
    ):
        try:
            return await self.repo.update(self.db, user_id, data)

        except IntegrityError as e:
            raise HTTPException(status_code=409, detail="username already exists")
