from sqlalchemy.dialects.mysql import DOUBLE, DATETIME, LONGBLOB, TEXT
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import time

time.sleep(3)

engine = create_engine(
    'mysql+mysqlconnector://duyphuoc:bebiu2020@127.0.0.1:3306/mydatabase')

Base = declarative_base()


class History(Base):
    '''History'''
    __tablename__ = "history"
    date = Column(DATETIME, primary_key=True)
    location = Column(TEXT)
    image = Column(LONGBLOB, default=None)

class Data(Base):
    '''History'''
    __tablename__ = "data"
    date = Column(DATETIME, primary_key=True)
    flow = Column(DOUBLE)
    pressure = Column(DOUBLE)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
