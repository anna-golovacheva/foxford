from sqlalchemy import JSON, Integer, MetaData, String, func
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.config import timestamp


class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[str] = mapped_column(String(length=20))
    figi: Mapped[str] = mapped_column(String(length=20))
    instrument_type: Mapped[str] = mapped_column(String(length=20), nullable=True)
    date: Mapped[timestamp] = mapped_column(server_default=func.now())
    type: Mapped[str] = mapped_column(String(length=20))
