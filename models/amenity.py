#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Blueprint for the amenity object """
    if models.env == 'db':
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
    else:
        name = ""
