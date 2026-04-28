from fastapi import APIRouter, Request, Depends

from dependencies.db import get_db
from dependencies.user_service import get_user_service
from schemas.user import CreateUserSchema, UserSchema
from services.user import UserService


router = APIRouter()


@router.post(
    "/create",
    response_model=UserSchema,
)
async def create_user(
    data: CreateUserSchema,
    db=Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return await service.create_user(db, data)
