#!/usr/bin/python3
"""
The base model for all vehicle items
which in one way inherit from this class
"""
import uuid
from sqlalchemy import String, Column
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel():
    """
    The base model
    """

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))

    def __init__(self):
        """
        constructor for the base model
        """
        self.id = str(uuid.uuid4())

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        attributes = { k: v for k, v in self.__dict__.items() }
        return f"[{self.__class__.__name__}] ({self.id}) {attributes}"
    
    def save(self):
        """
        Saves itself into storage
        """
        import models
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        return new_dict