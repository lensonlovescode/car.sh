#!/usr/bin/python3
"""
Contains a class definition for the manufacturer
which inherits from FuelType
"""
import uuid
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.model import Model


class Manufacturer(BaseModel, Base):
    """
    Manufacturers like Lamborghini, Ferarri yk the vibes.
    """

    __tablename__ = "manufacturers"

    name = Column(String(60), nullable=False)
    models = relationship("Model", back_populates="manufacturer", cascade="all, delete-orphan")

    def __init__(self, name):
        """
        constructor for the Manufacturer class
        """
        self.name = name
