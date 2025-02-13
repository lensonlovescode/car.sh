
## Database Structure

The database will be structured hierarchically to
categorize vehicles based on their type, fuel type, manufacturer, and specific models.

## Database Schema

### Categories Table

- Stores the primary classification of vehicles (e.g., SUVs, Sports Cars, Hatchbacks).

	1. id (Primary Key)
	2. category_name (e.g., SUVs, Hatchbacks, Convertibles)

### Fuel Types Table

- Links to categories, specifying whether a vehicle runs on petrol, diesel, or electricity.

	1. id (Primary Key)
	2. fuel_type (Petrol, Diesel, Electric)
	3. category_id (Foreign Key referencing Categories)

### Manufacturers Table

- Lists recognized car manufacturers under each fuel type.

	1. id (Primary Key)
	2. manufacturer_name (e.g., Toyota, BMW, Audi)
	3. fuel_type_id (Foreign Key referencing Fuel Types)

### Models Table
- Specific Models
	1. id (Primary Key)
	2. model_name (e.g., Corolla, X5, Model S)
	3. manufacturer_id (Foreign Key referencing Manufacturers)

## Python Hierchy

BaseModel (id)
 ├── Category (adds name)
 │    ├── FuelType (adds type, category_id)
 │    │    ├── Manufacturer (adds name, fueltype_id)
 │    │    │    ├── CarModel (adds name, year, price, manufacturer_id)

