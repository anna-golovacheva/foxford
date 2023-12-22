from fastapi_users import schemas
from typing import Optional


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    is_employee: bool = False
    tg_id: int

    if schemas.PYDANTIC_V2:  # pragma: no cover
        model_config = schemas.ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    is_employee: bool = False
    tg_id: int


# class UserUpdate(schemas.BaseUserUpdate):
#     pass