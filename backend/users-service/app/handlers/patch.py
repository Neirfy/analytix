from fastapi import APIRouter, Request, Depends
from uuid import UUID

from dependencies.db import get_db
from dependencies.user_service import get_user_service
from schemas.user import (
    UserSchema,
    UpdateUsernameSchema,
    UpdateEmailSchema,
    UpdatePhoneSchema,
)
from services.user import UserService


router = APIRouter()


@router.patch(
    "/{user_id}/username",
    response_model=UserSchema,
)
async def update_username(
    user_id: UUID,
    data: UpdateUsernameSchema,
    db=Depends(get_db),
    service: UserService = Depends(get_user_service),
) -> UserSchema:
    user_id = UUID("c28e1131-6a70-4f6c-8480-70d1b058ef55")  # HARDCODE
    return await service.update_username(db, user_id, data)


@router.patch(
    "/{user_id}/email",
    response_model=UserSchema,
)
async def update_email(
    user_id: UUID,
    data: UpdateEmailSchema,
    db=Depends(get_db),
    service: UserService = Depends(get_user_service),
) -> UserSchema:
    user_id = UUID("c28e1131-6a70-4f6c-8480-70d1b058ef55")  # HARDCODE
    return await service.update_email(db, user_id, data)


@router.patch(
    "/{user_id}/phone",
    response_model=UserSchema,
)
async def update_phone(
    user_id: UUID,
    data: UpdatePhoneSchema,
    db=Depends(get_db),
    service: UserService = Depends(get_user_service),
) -> UserSchema:
    user_id = UUID("c28e1131-6a70-4f6c-8480-70d1b058ef55")  # HARDCODE
    return await service.update_phone(db, user_id, data)
