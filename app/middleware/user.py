from app.settings.config import settings
from fastapi import FastAPI, Request, HTTPException, Depends
from sqlmodel import select
from app.models.user import User
from jwt import PyJWTError
import jwt
from app.settings.database import AsyncSessionLocal

async def current_user_middleware(request: Request, call_next):
    token = None
    authorization_header = request.headers.get("Authorization")
    if authorization_header and authorization_header.startswith("Bearer "):
        token = authorization_header[len("Bearer "):]
    
    if token:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            print("payload",payload)
            user_id = payload.get("user_id")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Invalid token")
        except PyJWTError:
            raise HTTPException(status_code=401, detail="PyJWTError:Invalid token")
        
           # Create an async database session
        async with AsyncSessionLocal() as db:
            user = await db.get(User, user_id)
            if user is None:
                raise HTTPException(status_code=401, detail="User not found")
            request.state.current_user = user
        del user.password
        request.state.current_user = user
    else:
        request.state.current_user = None
    
    response = await call_next(request)
    return response