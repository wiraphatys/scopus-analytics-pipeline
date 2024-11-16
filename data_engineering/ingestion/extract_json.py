# Extract data
import os
import json
from pkg.logger.logger_instance import Logger

def extract_json_data(year: int):
    log = Logger.get_logger("extract_json_data")
    log.info("Extracting data")

    folder_path = f"{os.getcwd()}/data/raw/{year}"
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                loaded_data = json.load(file)
                data.append(loaded_data)
    
    return data