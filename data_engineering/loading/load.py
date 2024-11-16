from pkg.database.mongo_connector import MongoConnector
from pkg.logger.logger_instance import Logger

def load_data(transformed_data) -> None:
    log = Logger.get_logger("load_data")
    log.info("Saving data")

    db = MongoConnector().connect()['research']
    db.insert_many(transformed_data)
