from fastapi import Depends
from dependencies.db import get_db

from service.user import UserService


def get_user_service(db=Depends(get_db)):
    return UserService(db)
