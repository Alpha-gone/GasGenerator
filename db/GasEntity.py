from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime


class GasEntity(declarative_base()):
    __tablename__ = 'gas'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    differential = Column(Float)
    pressure = Column(Float)
    date = Column(DateTime)
