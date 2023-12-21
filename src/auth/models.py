from typing import List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, Integer, String, Boolean, ForeignKey, MetaData, func
from src.database import Base
from src.config import timestamp


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    permissions: Mapped[JSON] = mapped_column(JSON, nullable=False)
    user: Mapped[List["User"]] = relationship("User", back_populates="roles")


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    username: Mapped[str] = mapped_column(
            String(length=20), unique=True, index=True, nullable=False
        )
    registered_at: Mapped[timestamp] = mapped_column(server_default=func.now())
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id, ondelete="CASCADE"))
    roles = relationship("Role", back_populates="user")
