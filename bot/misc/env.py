from os import environ
from typing import Final


class TgKeys:
    DB_URL: Final = environ.get("DB_URL", 'define me!')
    TOKEN: Final = environ.get('TOKEN', 'define me!')
