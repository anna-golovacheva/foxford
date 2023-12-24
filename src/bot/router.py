from sqlalchemy.dialects.postgresql import insert


# insert_statement = insert(User).values(
#         tg_id=message.from_user.id,
#         username=message.from_user.username,
#         hashed_password='123123'
#         )
#     do_nothing_stmt = insert_statement.on_conflict_do_nothing(index_elements=['tg_id'])
#     # db.query(table).get("id")
#     async with async_session_maker() as session:
#         print(">>> from tg file >>   ", session)
#         await session.execute(do_nothing_stmt)
#         await session.commit()