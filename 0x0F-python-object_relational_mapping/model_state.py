#!/usr/bin/python3
"""
This script contains the class definition of a State and
an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Creating  instance of the Base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
