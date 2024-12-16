from fastapi import APIRouter, Depends, HTTPException, status, Request
from datetime import datetime, timedelta
from app.schema.message import Message
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.settings.database import get_session
import uuid


router = APIRouter()

@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")