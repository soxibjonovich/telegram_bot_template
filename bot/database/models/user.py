import sqlalchemy as sa
from bot.database import Base


class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
