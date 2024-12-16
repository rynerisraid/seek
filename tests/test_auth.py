import pytest
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession


#创建用户
import pytest
from httpx import AsyncClient

# @pytest.mark.asyncio
# async def test_sign_up():
#     async with AsyncClient(base_url="http://localhost:8000") as ac:
#         response = await ac.post("/api/v1/auth/sign-up", json={
#             t"username": "testuser",
#             "email":"test@test.com",
#             "password": "tespassword"
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

@pytest.mark.asyncio
async def test_sign_in_success():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.post("/api/v1/auth/sign-in", json={
            "username": "testuser",
            "password": "testpassword"
        })

    """
    {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImV4cCI6MTczNDM4NDQ5Nn0.rmtFuKuL9xQTr7UhEDBwKxRLcIw8AzTG8G0_GjQkaVk",
    "token_type": "bearer"
    }
    """
    assert response.status_code == 200
    assert response.json()["detail"] == "Username already registered"

#重置密码

