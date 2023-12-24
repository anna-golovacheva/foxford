from fastapi import APIRouter, Request
import telebot
from src.config import BOT_SECRET
from src.bot.tg_utils import bot
router = APIRouter(
    prefix='/ticket',
    tags=['Ticket']
)

@router.post("/"+BOT_SECRET)
async def webhook(request: Request):
    chunks = []
    async for chunk in request.stream():
        chunks.append(chunk)

    # Combine the chunks and decode the content
    update = telebot.types.Update.de_json(b"".join(chunks).decode('utf-8'))
    print(update)
    bot.process_new_updates([update])
    return "ok ok ok"