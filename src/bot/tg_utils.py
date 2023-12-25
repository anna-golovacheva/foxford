import telebot
from sqlalchemy import select, insert
from src.config import BOT_TOKEN, BOT_SECRET, BASE_URL, GENERAL_EMPLOYEE
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

    stmt = Insert(User).values(tg_id=msg.from_user.id, username=msg.from_user.username, hashed_password='123123')
    print(stmt)
    session = get_sync_session()
    start_user = session.query(User).filter(User.tg_id == msg.from_user.id).first()
    print(start_user)
    if not start_user:
        result = session.execute(stmt)
        print(result)
        reply_message += str(result)
        session.commit()

    bot.send_message(msg.chat.id, reply_message)


@bot.message_handler(content_types=['text'])
def create_ticket(msg):
    session = get_sync_session()
    user = session.query(User).filter(User.tg_id == msg.from_user.id).first()
    if user:
        old_ticket = session.query(Ticket).filter(Ticket.client_id == user.id, Ticket.status == str(StatusType.open.name)).first()
        if old_ticket:
            message = 'Предыдущий тикет еще не закрыт'
        else:
            stmt = Insert(Ticket).values(client_id=user.id, status=str(StatusType.open.name), employee_id=7, message=msg.text)
            print(stmt)
            message = f'Тикет открыт .. {msg.text}'
            result = session.execute(stmt)
            print(result)
            session.commit()

    bot.send_message(msg.chat.id, message)







    # start_user = session.query(User).filter(User.tg_id == msg.from_user.id).first()
    # if not start_user:
        # start_user = User(tg_id=msg.from_user.id, username=msg.from_user.username, hashed_password='123123')
        # session.add(start_user)


            # a1 = result.scalars().first()


        # query = select(operation).where(operation.c.type == operation_type)