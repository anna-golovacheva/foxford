from src.database import Base
from sqlalchemy import Integer, String, func, Column, DateTime, Boolean

class User(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

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
