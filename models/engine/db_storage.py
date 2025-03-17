#!/usr/bin/python3
"""
Contains the database storage engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class Storage():
    """
    The database storage class
    """
    __session = None
    __engine = None

    def __init__(self):
       """
       The constructor method
       """
       self.__engine = create_engine("mysql+pymysql://carsh_dev:carsh%401hDbTVi4@localhost/carsh", pool_pre_ping=True)

       if getenv('env', default='production') == "test":
           Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session all
        objects depending on class name
        """
        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            classes = [Category, Manufacturer, FuelType, Model]
            for element in classes:
                query = self.__session.query(element)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj

        return objects

    def new(self, obj):
        """
        Add an object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload data and setup the database session
        """
        from models.base_model import Base
        from models.category import Category
        from models.manufacturer import Manufacturer
        from models.fuel_type import FuelType
        from models.model import Model
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """
        calls remove()
        """
        self.__session.remove()

    # def get(self, cls, id):
    #     """
    #     Returns the object based on the class name and its ID, or
    #     None if not found
    #     """
    #     if cls not in classes.values():
    #         return None

    #     all_cls = models.storage.all(cls)
    #     for value in all_cls.values():
    #         if (value.id == id):
    #             return value

    #     return None
