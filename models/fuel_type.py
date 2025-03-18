#!/usr/bin/python3
"""
Contains a class definition for the fuel type
which inherits from the BaseModel class
"""
import uuid
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.model import Model


class FuelType(BaseModel, Base):
    """
    Fuel type is either Petrol, Diesel or Electric
    Advanced versions should have these as classes
    but they will be stored as strings for now
    """

    __tablename__ = 'fuel_types'

    name = Column(String(60), nullable=False)
    models = relationship("Model", back_populates="fuel_type", cascade="all, delete-orphan")

    def __init__(self, name):
        """
        constructor for the FuelType class
        """
        self.name = name
