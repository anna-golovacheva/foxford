from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean, MetaData, func, Column, DateTime
from src.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(length=320), unique=True, index=True, nullable=True)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    is_employee = Column(Boolean, default=False, nullable=False)
    username = Column(String(length=20), unique=True, index=True, nullable=False)
    registered_at = Column(DateTime, server_default=func.now())
    tg_id = Column(Integer, nullable=True, index=True, unique=True)
