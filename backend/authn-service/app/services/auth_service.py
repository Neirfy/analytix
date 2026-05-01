from fastapi import HTTPException


async def login(data, db, redis, response):
    user = await users_client.get_user_by_username(data.username)

    if not verify_password(data.password, user.password):
        raise HTTPException(401)

    session_id = str(uuid.uuid4())

    await redis.setex(
        f"session:{session_id}",
        60 * 60 * 24,
        json.dumps({"user_id": user.id, "roles": user.roles}),
    )

    response.set_cookie("session_id", session_id, httponly=True)

    return {"ok": True}


async def validate(session_id: str, redis):
    data = await redis.get(f"session:{session_id}")

    if not data:
        raise HTTPException(401)

    return json.loads(data)


# async def authenticate_user(db, data):
#     user = await get_user_by_username(db, data.username)

#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     if not verify_password(data.password, user.password_hash):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     return user
