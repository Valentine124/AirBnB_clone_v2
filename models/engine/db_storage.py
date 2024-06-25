#!/usr/bin/python3

""" This module contains blueprints for the database """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

clsses = [State, City, User]

class DBStorage:
    """ The database object blueprint """

    __engine = None
    __session = None

    def __init__(self):
        """ The object initializer """
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        env = getenv('HBNB_ENV')
        connection_str = f'mysql+mysqldb://{usr}:{pwd}@{host}/{db}'
        self.__engine  = create_engine(connection_str, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """ return all objects from db depending on cls """
        objects = {}
        list = []

        if cls is not None:
            list.extend(self.__session.query(cls).all())
        else:
            for item in clsses:
                list.extend(self.__session.query(item).all())
        
        for obj in list:
            objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        
        return objects
    
    def new(self, obj):
        """ Add object to the current database """
        self.__session.add(obj)
    
    def save(self):
        """ Commits all transactions on the current database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete the obj from the current database if obj is not None """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """ Creates all tables and sessions """
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)

        self.__session = Session()