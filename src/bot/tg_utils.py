import telebot
from src.config import BOT_TOKEN, BOT_SECRET, BASE_URL, GENERAL_EMPLOYEE_ID, DEFAULT_PASS
from src.user.models import User
from src.tickets.models import Ticket
from src.tickets.schemas import StatusType
from src.database import get_sync_session
from sqlalchemy.dialects.postgresql import Insert


url = BASE_URL + BOT_SECRET

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)


@bot.message_handler(commands=['start'])
def start(msg):
    reply_message = 'Привет! С помощью этого бота вы можете '\
              'отправить сообщение-тикет. Просто напишите '\
              'сообщение.'

    stmt = Insert(User).values(
        tg_id=msg.from_user.id,
        username=msg.from_user.username,
        hashed_password=DEFAULT_PASS)
    session = get_sync_session()
    start_user = session.query(User).filter(
        User.tg_id == msg.from_user.id
        ).first()
    if not start_user:
        result = session.execute(stmt)
        reply_message += str(result)
        session.commit()

    bot.send_message(msg.chat.id, reply_message)


@bot.message_handler(content_types=['text'])
def create_ticket(msg):
    session = get_sync_session()
    user = session.query(User).filter(
        User.tg_id == msg.from_user.id
        ).first()
    if user:
        old_ticket = session.query(Ticket).filter(
            Ticket.client_id == user.id,
            Ticket.status.in_([
                StatusType.open.name,
                StatusType.in_progress.name
                ])
                ).first()
        if old_ticket:
            message = 'Предыдущий тикет еще не закрыт'
        else:
            stmt = Insert(Ticket).values(
                client_id=user.id,
                status=str(StatusType.open.name),
                employee_id=int(GENERAL_EMPLOYEE_ID),
                message=msg.text
                )
            message = 'Тикет открыт'
            session.execute(stmt)
            session.commit()

    bot.send_message(msg.chat.id, message)
