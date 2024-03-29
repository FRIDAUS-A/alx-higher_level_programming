#!/usr/bin/python3
"""a python file that contains the class
definition of a State and an instance Base =
declarative_base()
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """The class states which is mapped to a table in the database"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
