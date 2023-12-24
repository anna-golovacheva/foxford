import os
from datetime import datetime
from enum import Enum
from typing import Optional
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, Field
from src.auth.config import auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.config import fastapi_users

from src.tickets.router import router as router_ticket

import telebot
from src.config import BOT_TOKEN, BOT_SECRET, BASE_URL


app = FastAPI(
    title='Ticket Project'
)

url = BASE_URL + BOT_SECRET

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)


@app.post("/"+BOT_SECRET)
async def webhook(request: Request):
    chunks = []
    async for chunk in request.stream():
        chunks.append(chunk)

    # Combine the chunks and decode the content
    update = telebot.types.Update.de_json(b"".join(chunks).decode('utf-8'))
    print(update)
    bot.process_new_updates([update])
    return "ok ok ok"


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'hehehello')


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

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
