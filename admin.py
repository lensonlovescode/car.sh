#!/usr/bin/python3
"""
A cmd based tool for creating vehicle items and pushing to the database
"""
import cmd
from models import storage
from models.category import Category
from models.fuel_type import FuelType
from models.manufacturer import Manufacturer
from models.model import Model


class Carsh(cmd.Cmd):
    """
    Defines all commands
    """
    intro = "Welcome to Carsh Admin!"
    prompt = '(carsh) '

    def do_greet(self, arg):
        """
        Greets you
        """
        print("Hello Admin!")

    def do_create(self, arg):
        """
        Creates an item based on user input.
        """

        Items = {
            "manufacturer": Manufacturer,
            "category": Category,
            "fuel_type": FuelType,
            "model": Model
        }

        while True:
            item_type = input("Enter item type (manufacturer/category/fuel_type/model): ").strip().lower()

            if item_type not in Items:
                print("Invalid item type. Choose from: manufacturer, category, fuel_type, model.")
                continue

            if item_type == "manufacturer":
                name = input("Enter Manufacturer name: ").strip()
                obj = Manufacturer(name=name)

            elif item_type == "category":
                name = input("Enter Category name: ").strip()
                obj = Category(name=name)

            elif item_type == "fuel_type":
                valid_fuel_types = {"Diesel", "Petrol", "Electric", "Hybrid"}
                fuel = input("Enter Fuel Type (diesel/petrol/electric/hybrid): ").strip()
                if fuel not in valid_fuel_types:
                    print("Invalid fuel type. Choose from: diesel, petrol, electric, hybrid.")
                    continue
                obj = FuelType(name=fuel)

            elif item_type == "model":
                name = input("Enter Model name: ").strip()
                base_price = input("Enter Base Price: ").strip()
                if not base_price.isdigit():
                    print("Invalid price. Must be a number.")
                    continue
                base_price = int(base_price)

                ignition = input("Enter Ignition type: ").strip()

                fuel_type = input("Enter Fuel Type (Diesel/Petrol/Electric/Hybrid): ").strip()
                valid_fuel_types = {"Diesel", "Petrol", "Electric", "Hybrid"}
                if fuel_type not in valid_fuel_types:
                    print("Invalid fuel type. Choose from: Diesel, Petrol, Electric, Hybrid")
                    continue

                engine_capacity = input("Enter Engine Capacity (cc): ").strip()
                if not engine_capacity.isdigit():
                    print("Invalid engine capacity. Must be a number.")
                    continue
                engine_capacity = int(engine_capacity)

                category_id = input("Enter Category id: ").strip()

                m_id = input("Enter manufacturer id: ").strip()

                fuel_id = input("Enter Fuel id: ").strip()


                obj = Model(name=name, base_price=base_price, engine_capacity=engine_capacity,
                            ignition=ignition, category_id=category_id, fuel_type_id=fuel_id, manufacturer_id=m_id)

            obj.save()
            print(f"{item_type.capitalize()} '{obj.name}' created successfully!")
            break


    def do_exit(self, arg):
        """
        Exit
        """
        print("carshing out...")
        return True

if __name__ == '__main__':
    Carsh().cmdloop()