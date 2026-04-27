from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from models.user import UsersUser
from schemas.user import CreateUserSchema, UpdateUserSchema


class UserRepository:
    async def get_by_id(
        self,
        db: AsyncSession,
        user_id: UUID,
    ):
        result = await db.execute(select(UsersUser).where(UsersUser.id == user_id))
        return result.scalar_one_or_none()

    async def create(
        self,
        db: AsyncSession,
        data: CreateUserSchema,
    ):
        user = UsersUser(
            username=data.username,
            # email=data.email,
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user

    async def delete(
        self,
        db: AsyncSession,
        user_id: UUID,
    ):
        user = await self.get_by_id(db, user_id)

        if not user:
            return None

        await db.delete(user)
        await db.commit()

        return user

    async def update(
        self,
        db: AsyncSession,
        user_id: UUID,
        data: UpdateUserSchema,
    ):
        user = await self.get_by_id(db, user_id)

        if not user:
            return None

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(user, field, value)

        await db.commit()
        await db.refresh(user)

        return user
