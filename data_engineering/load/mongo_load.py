import os
from pkg.database.mongo_connector import MongoConnector
from pkg.logger.logger_instance import Logger
import json

def load_data_to_mongodb(transformed_data) -> None:
    log = Logger.get_logger("load_data_to_mongodb")
    log.info("Saving data to MongoDB")

    db = MongoConnector().connect()['openalex_research']
    db.insert_many(transformed_data)
