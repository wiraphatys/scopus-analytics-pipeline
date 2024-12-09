import os
from pkg.database.mongo_connector import MongoConnector
from pkg.logger.logger_instance import Logger
import json

def load_data_to_json(transformed_data) -> None:
    log = Logger.get_logger("load_data_to_json")
    log.info("Saving data to JSON file")

    filename = "./data/cleaned/cleaned_dataset.json"

    try:
        # Check if file exists
        if os.path.exists(filename):
            # Read existing data
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)

            # Extend existing data with new data
            existing_data.extend(transformed_data)
        else:
            # If file doesn't exist, use new data directly
            existing_data = transformed_data

        # Write combined data back to file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
