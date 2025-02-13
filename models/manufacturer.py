#!/usr/bin/python3
"""
Contains a class definition for the manufacturer
which inherits from FuelType
"""
import uuid
from base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


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
        super().__init__(self)
        self.name = name
