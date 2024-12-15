import uvicorn
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from api.v1.auth import router as auth_router
from sqlmodel import SQLModel
from settings.database import engine
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
# import sys
# sys.path.append('.')

# 加载 .env 文件
load_dotenv()

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    SQLModel.metadata.create_all(engine)
    print("create SQLmodel meta data")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router, prefix="/api/v1/auth",tags=["auth"])


@app.get('/')
async def read_root():
    return  {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)

