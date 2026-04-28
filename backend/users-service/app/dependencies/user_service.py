from fastapi import Depends

from repositories.user import UserRepository
from services.user import UserService


def get_user_repo():
    return UserRepository()


def get_user_service(repo=Depends(get_user_repo)):
    return UserService(repo)
