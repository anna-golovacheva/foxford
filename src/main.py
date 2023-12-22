from datetime import datetime
from enum import Enum
from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, Field
from src.auth.config import auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.config import fastapi_users

from src.tickets.router import router as router_ticket


app = FastAPI(
    title='Ticket Project'
)



# class DegreeType(Enum):
#     newbie = 'newbie'
#     expert = 'expert'

# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     type_degree: DegreeType

# class User(BaseModel):
#     id: int
#     role: str
#     name: str
#     degree: Optional[list[Degree]] = []

# @app.get('/users/{user_id}', response_model=list[User])
# def get_user(user_id: int):
#     return [user for user in fake_users if user.get('id') == user_id]


# @app.get('/trades')
# def get_trades(limit: int = 1, offset: int = 0):
#     return fake_trades[offset:][:limit]


# dake_users = [
#     {'id': 1, 'role': 'admin', 'name': 'Jack'},
#     {'id': 2, 'role': 'user', 'name': 'Bill'},
#     {'id': 3, 'role': 'user', 'name': 'Josh'}
# ]

# @app.post('/users/{user_id}')
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda x: x.get('id') == user_id, dake_users))[0]
#     current_user['name'] = new_name
#     return {'status': 200, 'data': current_user}

# class Trade(BaseModel):
#     id: int
#     user_id: int
#     currency: str = Field(max_length=5)
#     side: str
#     price: float = Field(ge=0)
#     amount: float


# @app.post('/trades')
# def add_trades(trades: list[Trade]):
#     fake_trades.extend(trades)
#     return {'status': 200, 'data': fake_trades}



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# current_active_user = fastapi_users.current_user(active=True)

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_active_user)):
#     return f"Hello, {user.username}"

# @app.get("/unprotected-route")
# def protected_route():
#     return "Hello, Puka"


app.include_router(router_ticket)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)