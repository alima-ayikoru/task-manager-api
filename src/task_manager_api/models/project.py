from src.task_manager_api.database import Base
from src.task_manager_api.models.user import User
from src.task_manager_api.models.task import Task
from src.task_manager_api.enums import ProjectStatus
from sqlalchemy import DateTime, ForeignKey, Enum as sqlalchemyEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Project(Base):
    __tablename__ = "projects"

    project_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    title: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    start_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    due_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[ProjectStatus] = mapped_column(sqlalchemyEnum(ProjectStatus), default=ProjectStatus.NOT_STARTED)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default= func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    user: Mapped["User"] = relationship("User", back_populates="projects")
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="project")

