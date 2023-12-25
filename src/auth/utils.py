from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from src.auth.models import User

from src.database import get_async_session

# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)

class CustomUserDatabase(SQLAlchemyUserDatabase[User]):
    def get_by_tg_id(self, db: Session, tg_id: int) -> User:
        return db.query(self.model).filter(self.model.tg_id == tg_id).first()
