from sqlalchemy import Column, Integer, BigInteger

from bot.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)