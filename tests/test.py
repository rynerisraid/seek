import pytest
from fastapi import APIRouter, Depends, HTTPException, status
from app.settings.database import get_session
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.user import UserResponse, UserCreate
from app.api.v1.auth import sign_up
from app.util.crypt import pwd_context

'''
pip install anyio
pip install pytest-asyncio
pip install pytest-tornasync
pip install pytest-trio
pip install pytest-twisted
'''