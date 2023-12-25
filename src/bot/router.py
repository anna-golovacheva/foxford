from fastapi import APIRouter, Request
import telebot
from src.config import BOT_SECRET
from src.bot.tg_utils import bot


router = APIRouter(
    tags=['Telegram']
)


@router.post("/" + BOT_SECRET)
async def webhook(request: Request):
    chunks = []
    async for chunk in request.stream():
        chunks.append(chunk)

    update = telebot.types.Update.de_json(b"".join(chunks).decode('utf-8'))
    bot.process_new_updates([update])
    return {"status": "ok"}