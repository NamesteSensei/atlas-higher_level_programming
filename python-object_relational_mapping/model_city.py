#!/usr/bin/python3
"""
Defines a City class to link to the MySQL table 'cities'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """
    City class that links to the 'cities' table.
    Attributes:
        id (int): City's id, auto-generated and primary key.
        name (string): City's name.
        state_id (int): Foreign key linking to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
