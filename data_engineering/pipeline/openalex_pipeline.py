from pkg.logger.logger_instance import Logger
from data_engineering.extract.openalex_ingestion import fetch_all_data
from data_engineering.transform.data_transformation import transform_data
from data_engineering.load.mongo_load import load_data_to_mongodb
from dotenv import load_dotenv

def run_openalex_pipeline():
    log = Logger.get_logger("run_openalex_pipeline")

    next_cursor = "*"
    while True:
        if next_cursor is None or not isinstance(next_cursor, str):
            break

        response_data = fetch_all_data(next_cursor)
        if response_data is not None:
            transformed_data = transform_data(response_data["results"])
            load_data_to_mongodb(transformed_data)
            log.info(f"cursor={next_cursor} page already uploaded data to MongoDB.")

            next_cursor = response_data["meta"].get("next_cursor", None)
            log.info(f"next_cursor={next_cursor}")


load_dotenv()
run_openalex_pipeline()
