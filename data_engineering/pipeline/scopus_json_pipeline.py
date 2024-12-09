from pkg.logger.logger_instance import Logger
from data_engineering.extract.json_ingestion import extract_json_data
from data_engineering.extract.openalex_ingestion import fetch_one_by_doi
from data_engineering.transform.data_transformation import transform_data
from data_engineering.load.mongo_load import load_data_to_mongodb
from dotenv import load_dotenv


def run_json_pipeline():
    log = Logger.get_logger("run_json_pipeline")
    log.info("Starting run json pipeline")

    doi_list = extract_json_data()

    for doi in doi_list:
        response = fetch_one_by_doi(doi)
        if response is None:
            continue

        transformed_data = transform_data([response])
        load_data_to_mongodb(transformed_data)


load_dotenv()
run_json_pipeline()