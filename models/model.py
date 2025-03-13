#!/usr/bin/python3
"""
Contains a class definition for the Model class
which inherits from the Manufacturer
"""
import uuid
from base_model import BaseModel
from sqlalchemy import Column, String, Inteer, ForeignKey
from sqlalchemy.orm import relationship

class Model(BaseModel):
    """
    Models like Escalade, Suburban yk the vibes.
    """

    __tablename__ = "models"

    name = Column(String(60), nullable=False)
    base_price = Column(Integer, nullable=False)
    ignition = Column(String(60), nullable=False)
    engine_capacity = Column(Integer, nullable=True)

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