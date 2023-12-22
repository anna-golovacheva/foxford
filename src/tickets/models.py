from typing import List
from sqlalchemy import JSON, ForeignKey, Integer, MetaData, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.auth.models import User
from src.database import Base
from src.config import timestamp


class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(String(length=15))
    client_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    employee_id: Mapped[str] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    created_at: Mapped[timestamp] = mapped_column(server_default=func.now())
    updated_at: Mapped[timestamp] = mapped_column(server_default=func.now())
    message: Mapped[str] = mapped_column(String())
    clients = relationship("User", foreign_keys=[client_id])
    employees = relationship("User", foreign_keys=[employee_id])
    tickets: Mapped[List["Response"]] = relationship("Response", back_populates="tickets")


class Response(Base):
    __tablename__ = "response"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey(Ticket.id, ondelete="CASCADE"))
    created_at: Mapped[timestamp] = mapped_column(server_default=func.now())
    message: Mapped[str] = mapped_column(String())
    tickets = relationship("Ticket")
