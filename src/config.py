import datetime
from typing import Annotated
from dotenv import load_dotenv
import os
import sys
from sqlalchemy import func
from sqlalchemy.orm import mapped_column


sys.path.append(os.path.join(sys.path[0], 'src'))

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

JWT_SECRET = os.environ.get('JWT_SECRET')
PASS_VER_SECRET = os.environ.get('PASS_VER_SECRET')

timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]