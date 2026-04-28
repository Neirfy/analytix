from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from uuid import UUID

from repositories.user import UserRepository
from schemas.user import (
    CreateUserSchema,
    UserSchema,
    UpdateUsernameSchema,
    UpdateEmailSchema,
    UpdatePhoneSchema,
)


class UserService:
    def __init__(self, repo):
        self.repo = repo

    async def get_me(
        self,
        db,
        user_id: UUID,
    ) -> UserSchema:
        user = await self.repo.get_by_id(db, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="user not found")

        return user

    async def create_user(
        self,
        db,
        data: CreateUserSchema,
    ) -> UserSchema:
        try:
            return await self.repo.create(db, data)

        except IntegrityError as e:
            raise HTTPException(status_code=409, detail="username already exists")

    async def delete_user(
        self,
        db,
        user_id: UUID,
    ):
        user = await self.repo.delete(db, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="user not found")

        return user

    async def update_username(
        self,
        db,
        user_id: UUID,
        data: UpdateUsernameSchema,
    ):
        try:
            return await self.repo.update(db, user_id, data)

        except IntegrityError as e:
            raise HTTPException(status_code=409, detail="username already exists")

    async def update_email(
        self,
        db,
        user_id: UUID,
        data: UpdateEmailSchema,
    ):
        # TODO отправка подтверждения

        return await self.repo.update(db, user_id, data)

    async def update_phone(
        self,
        db,
        user_id: UUID,
        data: UpdatePhoneSchema,
    ):
        # TODO SMS-код

        return await self.repo.update(db, user_id, data)
