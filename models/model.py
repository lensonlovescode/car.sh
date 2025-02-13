#!/usr/bin/python3
"""
Contains a class definition for the Model class
which inherits from the Manufacturer
"""
import uuid
from base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Model(BaseModel):
    """
    Models like Escalade, Suburban yk the vibes.
    """

    __tablename__ = "models"

    name = Column(String(60), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'))
    category = relationship("Category", back_populates="models", cascade="all, delete-orphan")
    fuel_type_id = Column(String(60), ForeignKey('fuel_types.id'))
    fuel_type = relationship("FuelType", back_populates="models", cascade="all, delete-orphan")
    manufacturer_id = Column(String(60), ForeignKey('manufacturers.id'))
    manufacturer = relationship("Manufacturer", back_populates="models", cascade="all, delete-orphan")


    def __init__(self, model_name):
        """
        constructor for the category class
        """
        super().__init__(self)
        self.name = model_name
