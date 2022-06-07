from typing import Optional
from fastapi import Form
from pydantic import BaseModel


class BaseUsers(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    password: str

    @classmethod
    def as_form(cls, name: str = Form(...), username: str = Form(...), password: str = Form(...)):
        return cls(name=name, username=username, password=password)

    @classmethod
    def as_login(cls, username: str = Form(...), password: str = Form(...)):
        return cls(username=username, password=password)


class AddUsers(BaseUsers):
    pass


class User(BaseUsers):
    username: str
    password: str

    class Config:
        orm_mode = True
