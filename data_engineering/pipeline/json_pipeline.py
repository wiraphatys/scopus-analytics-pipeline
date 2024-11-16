from pkg.logger.logger_instance import Logger
from data_engineering.ingestion.extract_json import extract_json_data
from data_engineering.transformation.transfrom import transform_data
from data_engineering.loading.load import load_data
from dotenv import load_dotenv

YEARS_OF_JSON_SCOPUS_DATA = [2018, 2019, 2020, 2021, 2022, 2023]

def run_json_pipeline():
    log = Logger.get_logger("data_pipeline.json")

    for year in YEARS_OF_JSON_SCOPUS_DATA:
        log.info(f"Starting JSON data pipeline for the year {year}")

        raw_data = extract_json_data(year)
        transformed_data = transform_data(raw_data)
        load_data(transformed_data)

        log.info(f"Successfully loaded data for year {year}")


load_dotenv()
run_json_pipeline()