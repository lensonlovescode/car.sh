import uuid
from models import storage
from models.model import Model

# List of Toyota models
toyota_models = [
    "Toyota bZ",
    "Toyota 4Runner",
    "Toyota Yaris 5 Doors",
    "Toyota GR Yaris",
    "Toyota Camry",
    "Toyota Tacoma",
    "Toyota Yaris Cross",
    "Toyota C-HR",
    "Toyota Sequoia",
    "Toyota Corolla Cross",
    "Toyota Prius",
    "Toyota Corolla Touring",
    "Toyota Corolla Sedan",
    "Toyota Tundra",
    "Toyota Mirai",
    "Toyota Hilux Double Cab",
    "Toyota Land Cruiser Prado",
    "Toyota Sienna",
    "Toyota Avalon",
    "Toyota Aygo 5 Doors",
    "Toyota Auris 5 Doors",
    "Toyota Yaris Sedan",
    "Toyota Highlander Kluger",
    "Toyota RAV4 5 Doors",
    "Toyota Venza",
    "Toyota GT 86",
    "Toyota Corolla (US)",
    "Toyota Avensis Wagon",
    "Toyota Fortuner",
    "Toyota Urban Cruiser",
    "Toyota Avensis",
    "Toyota Previa Estima",
    "Toyota Supra",
    "Toyota Crown",
    "Toyota Etios",
    "Toyota Corolla Cross (US)",
    "Toyota Harrier",
    "Toyota Crown SUV",
    "Toyota Etios Liva",
    "Toyota Vios",
    "Toyota Century SUV",
    "Toyota Grand Highlander",
    "Toyota Aygo X",
    "Toyota Rukus",
    "Toyota Aqua",
    "Toyota Century Sedan",
    "Toyota VERSO-S",
    "Toyota Agya",
    "Toyota GR 86",
    "Toyota GR Supra",
    "Toyota Yaris Hatchback",
    "Toyota GR Corolla",
    "Toyota Alphard",
    "Toyota Aurion",
    "Toyota Auris 3 Doors",
    "Toyota Auris Touring",
    "Toyota Avensis Liftback",
    "Toyota Avensis Verso",
    "Toyota Aygo 3 Doors",
    "Toyota Celica",
    "Toyota Celica Convertible",
    "Toyota Corolla",
    "Toyota Corolla 3 Doors",
    "Toyota Corolla 5 Doors",
    "Toyota Corolla Liftback",
    "Toyota Corolla Verso",
    "Toyota Corolla Wagon",
    "Toyota FJ Cruiser",
    "Toyota Hilux",
    "Toyota Hilux Extra Cab",
    "Toyota Hilux Single Cab",
    "Toyota Innova",
    "Toyota iQ",
    "Toyota Land Cruiser V8",
    "Toyota Matrix",
    "Toyota MR2",
    "Toyota MR2 Cabriolet",
    "Toyota Paseo",
    "Toyota Picnic",
    "Toyota Prius C (Aqua)",
    "Toyota Prius Prime",
    "Toyota Prius v/Prius+",
    "Toyota RAV4 3 Doors",
    "Toyota Solara Convertible",
    "Toyota Starlet 3 Doors",
    "Toyota Starlet 5 Doors",
    "Toyota Verso",
    "Toyota Yaris 3 Doors",
    "Toyota Yaris TS 3 Doors",
    "Toyota Yaris TS 5 Doors",
    "Toyota Yaris Verso"
]

# Example mappings (replace with actual data)
category_mapping = {
    "suvs": "fea43b0a-c6d6-48df-a96b-7cf210d85329",
    "hatchbacks": "6b23b27d-5072-47f0-8e61-b57063a74c6d",
    "sedans": "34cc611a-4b9d-40dc-b286-0541ffdb4bf5",
    "trucks": "55f96e65-88d7-460a-b4b1-4c1c214c7a83",
    "vans": "d241a35d-0789-49db-998e-b63d761b926f",
    "wagons": "962f8b1e-4c0a-42c2-a86f-d694db54b448",
    "coupes": "ec55a5dd-efbc-4310-9208-181864c3723e",
    "convertibles": "74a319f9-994a-4c29-8e8a-9fab49b0055a"
}

fuel_type_mapping = {
    "Gasoline": "ba05f2e0-0845-4947-bded-e7f65b5099a5",
    "Diesel": "e70c978c-99ad-49b4-bdb4-b872c014c0d6",
    "Hybrid": "394e0b48-1780-4a3a-a038-c21288eb9cea",
    "Electric": "53c7b960-7b2b-4735-b612-b086e672090f"
}

manufacturer_id = "2547391f-133f-419d-99a3-900396c86f18"  # Toyota's manufacturer ID

# Function to create and save model instances
def create_and_save_models():
    for model_name in toyota_models:
        # Extract base price, ignition, engine capacity, category, and fuel type
        base_price = 0  # Replace with actual base price
        ignition = "Electric"  # Replace with actual ignition type
        engine_capacity = 0  # Replace with actual engine capacity
        category_name = "suvs"  # Replace with actual category
        fuel_type_name = "Electric"  # Replace with actual fuel type

        # Retrieve category and fuel type IDs
        category_id = category_mapping.get(category_name, None)
        fuel_type_id = fuel_type_mapping.get(fuel_type_name, None)

        # Ensure all required fields are available
        if None in (category_id, fuel_type_id):
            print(f"Skipping {model_name} due to missing category or fuel type.")
            continue

        # Create a new Model instance
        model_instance = Model(
            id=str(uuid.uuid4()),
            name=model_name,
            base_price=base_price,
            ignition=ignition,
            engine_capacity=engine_capacity,
            category_id=category_id,
            fuel_type_id=fuel_type_id,
            manufacturer_id=manufacturer_id,
        )

        # Save the model instance
        storage.new(model_instance)
        storage.save()
        print(f"Saved model: {model_name}")

# Run the function
create_and_save_models()
