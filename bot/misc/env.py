from os import environ
from dotenv import load_dotenv
from typing import Final

load_dotenv()

class TgKeys:
    DB_URL: Final = environ.get("DB_URL", 'define me!')
    TOKEN: Final = environ.get('TOKEN', 'define me!')
    ADMINS: Final = environ.get('ADMINS', 'define me!')
