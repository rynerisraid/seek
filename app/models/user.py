from typing import Optional, Union
import uuid
from sqlmodel import Field, SQLModel,select
from datetime import datetime
from enum import Enum

class UserRole(str,Enum):
    admin = "admin"
    member = "member"

    
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(index=True, nullable=False, unique=True, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password: str = Field(nullable=False)
    role: UserRole = Field(default=UserRole.member) 
    status: str = Field(default="active")
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)  # 默认值
    updated_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now}) 


    def __repr__(self) -> str:
        return f"<User username={self.username} email={self.email}>"
    