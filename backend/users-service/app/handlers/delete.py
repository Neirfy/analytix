from fastapi import APIRouter, Request, Depends
from uuid import UUID

from dependencies.db import get_db
from dependencies.user_service import get_user_service
from schemas.user import UserSchema
from services.user import UserService


router = APIRouter()


@router.delete(
    "/{user_id}/delete",
    response_model=UserSchema,
)
async def delete_user(
    user_id: UUID,
    db=Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return await service.delete_user(db, user_id)
