from typing import List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, Integer, String, Boolean, ForeignKey, MetaData, func
from src.database import Base
from src.config import timestamp
# import src.operations.models as m

# Tickets = m.Ticket


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=True
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
    is_employee: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    username: Mapped[str] = mapped_column(
            String(length=20), unique=True, index=True, nullable=False
        )
    registered_at: Mapped[timestamp] = mapped_column(server_default=func.now())
    tg_id: Mapped[int] = mapped_column(Integer, nullable=True)
    # ticket: Mapped[List["Ticket"]] = relationship("Ticket", back_populates="user")
    # ticket: Mapped[List["Ticket"]] = relationship("Ticket", back_populates="employees")
