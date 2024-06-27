#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', 
                             String(60), 
                             ForeignKey('places.id'), 
                             primary_key=True, 
                             nullable=False
                             ),
                      Column('amenity_id', 
                             String(60), 
                             ForeignKey('amenities.id'), 
                             primary_key=True, 
                             nullable=False
                             )
                      )
class Place(BaseModel, Base):
    """ A place to stay """
    if models.env == 'db':
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, backref='place_amenity')
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Returns the list of review instances with place_id equals to the current place """
            list = []

            all_review = models.storage.all(Review).values()
            all_place = models.storage.all(Place).values

            for v_place in all_place:
                for v_review in all_review:
                    if v_review.place_id == v_place.id:
                        list.append(v_review)
            return list
        
        @property
        def amenities(self):
            """ Returns the list of amenity instance that contains all amenity.id linked to Place """
            all_amenity = models.storage.all(Amenity).values()
            amenity_list = []

            for amenity in all_amenity:
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            
            return amenity_list
        
        @amenities.setter
        def amenities(self, amenity_obj):
            """ Set amenity.id in amenities.ids"""
            if type(amenity_obj) is Amenity:
                self.amenity_ids.append(amenity_obj.id)