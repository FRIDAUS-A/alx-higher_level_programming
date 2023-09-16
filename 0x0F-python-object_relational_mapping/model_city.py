#!/usr/bin/python3
"""
a Python file similar to model_state.py named
model_city.py that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from model_state import Base, State


class City(Base):
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
