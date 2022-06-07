from ..schemas.users import *
from ..model.users import Users
from sqlalchemy.orm import Session


class HandUser:
    async def create_user(db: Session, item: AddUsers):
        user = Users(name=item.name, username=item.username, password=item.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user(db: Session, item: User):
        return db.query(Users).filter(Users.username == item.username, Users.password == item.password).first()

    def get_username(db: Session, _username):
        return db.query(Users).filter(Users.username == _username).first()
