from typing import List
from sqlalchemy import JSON, ForeignKey, Integer, MetaData, String, func, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.auth.models import User
from src.database import Base
from src.config import timestamp


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True)
    status = Column(String(length=15))
    client_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    employee_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())
    message = Column(String())

    clients = relationship("User", foreign_keys=[client_id])
    employees = relationship("User", foreign_keys=[employee_id])
    tickets = relationship("Response", back_populates="ticket")


class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey("ticket.id", ondelete="CASCADE"))
    created_at = Column(DateTime, server_default=func.now())
    message = Column(String())

    ticket = relationship("Ticket", back_populates="responses")
