import datetime
from typing import Annotated
from dotenv import load_dotenv
import os
import sys
from sqlalchemy import func


load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

JWT_SECRET = os.environ.get('JWT_SECRET')
PASS_VER_SECRET = os.environ.get('PASS_VER_SECRET')

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_SECRET = os.environ.get('BOT_SECRET')

BASE_URL = os.environ.get('BASE_URL')

# plug untill picking an employee user logic is realised
GENERAL_EMPLOYEE_ID = os.environ.get('GENERAL_EMPLOYEE_ID')

DEFAULT_PASS = os.environ.get('DEFAULT_PASS')