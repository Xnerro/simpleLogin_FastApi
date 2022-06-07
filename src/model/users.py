from sqlalchemy import Column, Integer, String
from .db import base


class Users(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    username = Column(String(25), unique=True)
    password = Column(String(25))

    def __repr__(self):
        return f"User : {self.name}, {self.username}, {self.password}"
