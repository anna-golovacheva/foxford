# import telebot
# from sqlalchemy import select, insert
# from src.config import BOT_TOKEN, BOT_SECRET, BASE_URL
# from src.user.models import User
# from src.database import get_async_session

# url = BASE_URL + BOT_SECRET

# bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
# bot.remove_webhook()
# bot.set_webhook(url=url)


# @bot.message_handler(commands=['start'])
# async def start(msg):
#     reply_message = 'Привет! С помощью этого бота вы можете '\
#               'отправить сообщение-тикет. Просто напишите '\
#               'сообщение.'
#     stmt = insert('src.user.models.User').values(tg_id=msg.from_user.id, username=msg.from_user.username, hashed_password='123123')

#     async with get_async_session() as session:
#         stmt = stmt.on_conflict_do_nothing(constraint="tg_id")
#         result = await session.execute(stmt)
#         print(result)
#         reply_message += str(result)
#         await session.commit()

#     await bot.send_message(msg.chat.id, reply_message)


import telebot
import asyncio
from sqlalchemy import insert
from src.config import BOT_TOKEN, BOT_SECRET, BASE_URL
from src.user.models import User
from src.database import get_async_session

url = BASE_URL + BOT_SECRET

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

@bot.message_handler(commands=['start'])
def start(msg):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    reply_message = 'Привет! С помощью этого бота вы можете '\
              'отправить сообщение-тикет. Просто напишите '\
              'сообщение.'
    stmt = insert(User).values(tg_id=msg.from_user.id, username=msg.from_user.username, hashed_password='123123')

    async def process_start():
        async with get_async_session() as session:
            stmt = stmt.on_conflict_do_nothing(constraint="tg_id")
            result = await session.execute(stmt)
            print(result)
            await session.commit()

        await bot.send_message(msg.chat.id, reply_message)

    loop.run_until_complete(process_start())


# @dp.message(Command(commands='help'))
# async def process_help_command(message: Message):
#     await message.answer("help text")
#     insert_statement = insert(User).values(
#         tg_id=message.from_user.id,
#         username=message.from_user.username
#         )
#     do_nothing_stmt = insert_statement.on_conflict_do_nothing(index_elements=['tg_id'])
#     # db.query(table).get("id")
#     await session.execute(do_nothing_stmt)
#     await session.commit()


# @dp.message(Command(commands='cancel'))
# async def process_cancel_command(message: Message):
#     user = User.get_or_create(message.from_user)

#     if user.is_active:
#         user.is_active = False
#         await message.answer(answer_ru.play_cancel)
#     else:
#         await message.answer(answer_ru.not_play_cancel)


# @dp.message(F.text.lower().in_(answer_ru.yes_list))
# async def process_positive_answer(message: Message):
#     user = User.get_or_create(message.from_user)
#     if not user.is_active:
#         user.is_active = True
#         number = get_random_number()
#         Game.create(user.pk, number)
#         await message.answer(answer_ru.got_number)
#     else:
#         await message.answer(answer_ru.in_game)


# @dp.message(F.text.lower().in_(answer_ru.no_list))
# async def process_negative_answer(message: Message):
#     user = User.get_or_create(message.from_user)
#     if not user.is_active:
#         await message.answer(answer_ru.no)
#     else:
#         await message.answer(answer_ru.in_game)


# @dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
# async def process_numbers_answer(message: Message):
#     user = User.get_or_create(message.from_user)
#     if user.is_active:
#         game = Game.get_object({'user_id': user.pk, 'is_active': 'True'})
#         print(game)
#         if int(message.text) == game.number:
#             user.is_active = False
#             game.is_win = True
#             game.is_active = False
#             user.games_num += 1
#             user.wins_num += 1
#             await message.answer(answer_ru.win)
#         elif int(message.text) > game.number:
#             game.tries_num -= 1
#             await message.answer(answer_ru.less)
#         elif int(message.text) < game.number:
#             game.tries_num -= 1
#             await message.answer(answer_ru.more)

#         if game.tries_num == 0:
#             game.is_active = False
#             user.is_active = False
#             user.games_num += 1
#             await message.answer(answer_ru.loss(game.number))
#     else:
#         await message.answer(answer_ru.number_outside_game)


# @dp.message(Command(commands='stat'))
# async def process_stat_command(message: Message):
#     user = User.get_or_create(message.from_user)
#     all_users = User.get_all()
#     if all_users:
#         sorted_users = sorted(all_users, key=lambda x: x.wins_num, reverse=True)
#         place = sorted_users.index(user) + 1
#     await message.answer(answer_ru.stat(user.games_num, user.wins_num, place))


# @dp.message()
# async def process_other_answers(message: Message):
#     user = User.get_or_create(message.from_user)
#     if user.is_active:
#         await message.answer(answer_ru.in_game)
#     else:
#         await message.answer(answer_ru.extra)





    # start_user = session.query(User).filter(User.tg_id == msg.from_user.id).first()
    # if not start_user:
        # start_user = User(tg_id=msg.from_user.id, username=msg.from_user.username, hashed_password='123123')
        # session.add(start_user)


            # a1 = result.scalars().first()


        # query = select(operation).where(operation.c.type == operation_type)