# src/task_manager_api/models/user.py
from src.task_manager_api.database import Base
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True) 
    hashed_password: Mapped[str] = mapped_column()
    is_verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default= func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))   
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    projects: Mapped[list["Project"]] = relationship("Project", back_populates="user")
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="user")
