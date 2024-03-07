from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class Statistics(Base):
    __tablename__ = "statistics"

    date = Column(DateTime, primary_key=True)
    flow = Column(Float)
    pressure = Column(Float)
