from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.config import auth_backend
from src.auth.schemas import UserRead, UserCreate
# from src.auth.models import User
# from src.auth.manager import get_user_manager
from src.auth.config import fastapi_users

from src.tickets.router import router as router_ticket
from src.bot.router import router as router_bot


app = FastAPI(
    title='Ticket Project'
)

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

app.include_router(router_ticket)

app.include_router(router_bot)


origins = [
   ['*'],
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
