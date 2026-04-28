import pytest
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from uuid import uuid4
from unittest.mock import AsyncMock

from services.user import UserService
from schemas.user import CreateUserSchema, UserSchema, UpdateUserSchema


@pytest.mark.asyncio
async def test_create_user(mock_repo):
    input_data = CreateUserSchema(username="test")

    mock_repo.create = AsyncMock(return_value={"username": "test"})

    service = UserService(mock_repo)

    result = await service.create_user(db=None, data=input_data)

    # проверка результата
    assert result == {"username": "test"}

    # проверка вызова
    mock_repo.create.assert_awaited_once()

    call_args = mock_repo.create.await_args

    assert call_args is not None, "repo.create не был вызван"
    args, kwargs = call_args

    assert args[0] is None  # db
    assert args[1] == input_data  # data


@pytest.mark.asyncio
async def test_create_user_conflict(mock_repo):
    input_data = CreateUserSchema(username="test")

    mock_repo.create.side_effect = IntegrityError(
        "INSERT INTO users ...",
        params=None,
        orig=Exception("unique constraint failed"),
    )

    service = UserService(mock_repo)

    with pytest.raises(HTTPException) as exc:
        await service.create_user(db=None, data=input_data)

    assert exc.value.status_code == 409
    assert exc.value.detail == "username already exists"


@pytest.mark.asyncio
async def test_get_me_success(mock_repo):
    user_id = uuid4()
    fake_user = {"id": user_id, "username": "test"}

    mock_repo.get_by_id = AsyncMock(return_value=fake_user)

    service = UserService(mock_repo)

    result = await service.get_me(db=None, user_id=user_id)

    assert result == fake_user

    mock_repo.get_by_id.assert_awaited_once_with(None, user_id)


@pytest.mark.asyncio
async def test_get_me_not_found(mock_repo):
    mock_repo.get_by_id = AsyncMock(return_value=None)

    service = UserService(mock_repo)

    with pytest.raises(HTTPException) as exc:
        await service.get_me(db=None, user_id=uuid4())

    assert exc.value.status_code == 404
    assert exc.value.detail == "user not found"


@pytest.mark.asyncio
async def test_update_username(mock_repo):
    user_id = uuid4()

    update_data = UpdateUserSchema(username="test")
    updated_user = UserSchema(username="new_name")

    mock_repo.update.return_value = updated_user

    service = UserService(mock_repo)

    result = await service.update_username(
        db=None,
        user_id=user_id,
        data=update_data,
    )

    assert result == updated_user
    mock_repo.update.assert_awaited_once_with(None, user_id, update_data)


@pytest.mark.asyncio
async def test_delete_user(mock_repo):
    user_id = uuid4()

    mock_repo.delete.return_value = True

    service = UserService(mock_repo)

    result = await service.delete_user(db=None, user_id=user_id)

    assert result is True
    mock_repo.delete.assert_awaited_once_with(None, user_id)
