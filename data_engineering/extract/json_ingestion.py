import os
import json
import requests
from pkg.logger.logger_instance import Logger
from pkg.helper.dict_helper import safe_get_nested

YEARS_OF_JSON_SCOPUS_DATA = [2018, 2019, 2020, 2021, 2022, 2023]

def extract_json_data() -> list[str]:
    log = Logger.get_logger("extract_json_data")
    log.info("Extracting data")

    data = []
    counter = 1

    for year in YEARS_OF_JSON_SCOPUS_DATA:
        folder_path = f"{os.getcwd()}/data/raw/{year}"
        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    doi = safe_get_nested(loaded_data, ["abstracts-retrieval-response", "coredata", "prism:doi"])
                    data.append(doi)

                    log.info(f"already added for {counter} items")
                    counter += 1
    
    return data