from typing import Optional
import uuid
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

class Workspace(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(nullable=False)
    created_by: Optional[int] = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, 
                                 sa_column_kwargs={"onupdate": datetime.now})
    
    # 假设存在 User 模型
    creator: Optional["User"] = Relationship(back_populates="workspaces_created", 
                                             sa_relationship_kwargs={"lazy": "joined"})
    
    def __repr__(self) -> str:
        return f"<Workspace name={self.name} id={self.id}>"