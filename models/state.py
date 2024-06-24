#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.env == "db":
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        citie = relationship("City", backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """ Return all cities with state_id equal to current state.id"""
            list = []
            states = all(State)
            citys = all(City)

            for val in states.values():
                for city_val in citys.values():
                    if val.id == city_val.state_id:
                        list.append(city_val)
        
            return list
