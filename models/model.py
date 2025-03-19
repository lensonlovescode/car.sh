#!/usr/bin/python3
"""
Contains a class definition for the Model class
which inherits from the Manufacturer
"""
import uuid
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base


class Model(BaseModel, Base):
    """
    Models like Escalade, Suburban yk the vibes.
    """

    __tablename__ = "models"

    name = Column(String(60), nullable=False)
    base_price = Column(Integer, nullable=False)
    ignition = Column(String(60), nullable=False)
    engine_capacity = Column(Integer, nullable=True)

    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="models")

    fuel_type_id = Column(String(60), ForeignKey('fuel_types.id'), nullable=False)
    fuel_type = relationship("FuelType", back_populates="models")

    manufacturer_id = Column(String(60), ForeignKey('manufacturers.id'), nullable=False)
    manufacturer = relationship("Manufacturer", back_populates="models")


    def __init__(self, name, base_price, engine_capacity, ignition, category_id, fuel_type_id, manufacturer_id):
        """
        constructor for the category class
        """
        self.name = name
        self.base_price = base_price
        self.fuel_type_id = fuel_type_id
        self.engine_capacity = engine_capacity
        self.ignition = ignition
        self.category_id = category_id
        self.manufacturer_id = manufacturer_id

    def calculate(self):
        """
        Calculates the final shipping cost of the model.
        Includes Import Duty, Excise Duty, VAT, Import Declaration Fees, and Railway Development Levy.
        """
        import_duty = 0.25 * self.base_price
        
        if self.fuel_type == "Electric":
            excise_duty = 0.10 * self.base_price
        elif self.fuel_type == "Hybrid":
            excise_duty = 0.25 * self.base_price
        elif self.fuel_type == "Petrol":
            if self.engine_capacity <= 1500:
                excise_duty = 0.20 * self.base_price
            elif self.engine_capacity <= 3000:
                excise_duty = 0.25 * self.base_price
            else:
                excise_duty = 0.35 * self.base_price
        elif self.fuel_type == "Diesel":
            if self.engine_capacity <= 1500:
                excise_duty = 0.25 * self.base_price
            elif self.engine_capacity <= 2500:
                excise_duty = 0.25 * self.base_price
            else:
                excise_duty = 0.35 * self.base_price
        else:
            excise_duty = 0

        vat = 0.16 * (self.base_price + import_duty + excise_duty)

        import_declaration_fees = 0.035 * self.base_price

        railway_levy = 0.02 * self.base_price

        total_cost = (
            self.base_price +
            import_duty +
            excise_duty +
            vat +
            import_declaration_fees +
            railway_levy
        )

        return total_cost
