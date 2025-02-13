#!/usr/bin/python3
"""
Contains a class definition for the categories
which inherit from the base model
"""
import uuid
from base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class Category(BaseModel, Base):
    """
    Categories like SUVs, Sedans, Hatchbacks etc.
    """

    __tablename__ = 'categories'

    name = Column(String(60), nullable=False)
    models = relationship("Model", back_populates="category", cascade="all, delete-orphan")


    def __init__(self, name):
        """
        constructor for the category class
        """
        super().__init__(self)
        self.name = name
