from sqlalchemy.dialects.mysql import FLOAT, DATETIME, TINYBLOB, CHAR
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import time

time.sleep(3)

engine = create_engine(
    'mysql+mysqlconnector://phuocvnd:phuocvnd@192.85.4.173:3307/mydatabase')

Base = declarative_base()


class History(Base):
    '''History'''
    __tablename__ = "history"
    date = Column(DATETIME, primary_key=True)
    location = Column(CHAR)
    image = Column(TINYBLOB, default=None)


class Data(Base):
    '''History'''
    __tablename__ = "data"
    date = Column(DATETIME, primary_key=True)
    pressure = Column(FLOAT)
    flow = Column(FLOAT)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
