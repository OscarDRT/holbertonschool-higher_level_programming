#!/usr/bin/python3
"""model state"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """class state"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """__repr__"""
        return "<State(id='%d', name='%s')>" % (self.id, self.name)
