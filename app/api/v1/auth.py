from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta
from app.schema.message import Message
from app.models.user import User
from app.settings.database import get_session
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.user import UserResponse, UserCreate,LoginRequest
from app.util.crypt import pwd_context

router = APIRouter()

@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")


@router.post("/sign-up", response_model=UserResponse)
async def sign_up(user: UserCreate,session:AsyncSession = Depends(get_session)):
    #检查用户名是否存在
    query = select(User).where(User.username == user.username or User.email == user.email)
    result = await session.execute(query)
    db_user = result.scalars().first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    # 创建新用户
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return UserResponse(id=db_user.id,username=db_user.username,email=db_user.email)


@router.post("/sign-in", response_model=UserResponse)
async def sign_in(user: LoginRequest,session:AsyncSession = Depends(get_session)):
    # 检查用户名是否存在
    query = select(User).where(User.username == user.username)
    result = await session.execute(query)
    db_user = result.scalars().first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or password is incorrect")
    
    # 检查密码是否正确
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or password is incorrect")
    
    # 返回用户信息
    return UserResponse(id=db_user.id,username=db_user.username,email=db_user.email)
