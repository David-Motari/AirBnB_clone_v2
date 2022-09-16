#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import environ


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    SELECTED_STORAGE = environ.get("HBNB_TYPE_STORAGE")
    if SELECTED_STORAGE == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
