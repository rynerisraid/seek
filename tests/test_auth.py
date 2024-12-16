import pytest
from fastapi import APIRouter, Depends, HTTPException, status
from app.settings.database import get_session
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.user import UserResponse, UserCreate
from app.api.v1.auth import sign_up
from app.util.crypt import pwd_context


#创建用户
import pytest
from httpx import AsyncClient
from app.main import app

# @pytest.mark.asyncio
# async def test_sign_up():
#     async with AsyncClient(base_url="http://localhost:8000") as ac:
#         response = await ac.post("/api/v1/auth/sign-up", json={
#             "username": "testuser",
#             "email":"test@test.com",
#             "password": "testpassword"
#         })
#     assert response.status_code == 200
#     assert "id" in response.json()
#     assert response.json()["username"] == "testuser"
#     assert "created_at" in response.json()
#     assert "updated_at" in response.json()

@pytest.mark.asyncio
async def test_sign_up_already_registered():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.post("/api/v1/auth/sign-up", json={
            "username": "testuser",
            "email":"test@test.com",
            "password": "testpassword"
        })
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"

#登录


#重置密码

