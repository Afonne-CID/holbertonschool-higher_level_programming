#!/usr/bin/python3
""" Contains the class definition of a State and an instance \
        `Base = declaraltive()`
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Represents a 'state' for a MySQL database
        and inherits from the `Base` class

    __tablename__ (str): The name of the MySQL table to store state into.
    id (int): State id
    name (String): State name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
