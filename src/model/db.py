from requests import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root@localhost:3306/test")

base = declarative_base()

session = sessionmaker(autocommit=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
