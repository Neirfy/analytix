from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from dependencies.db import get_db
from dependencies.user_service import get_user_service
from schemas.user import UserSchema
from services.user import UserService


router = APIRouter()


@router.get(
    "/me",
    response_model=UserSchema,
)
async def get_me(
    # user_id: UUID,
    request: Request,
    db: AsyncSession = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    # user_id = UUID("c28e1131-6a70-4f6c-8480-70d1b058ef55")  # HARDCODE
    user_id = request.headers.get("X-User-Id")

    if not user_id:
        raise HTTPException(status_code=401, detail="unauthorized")
    return await service.get_me(db, user_id)
