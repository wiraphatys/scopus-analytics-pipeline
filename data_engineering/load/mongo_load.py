from pkg.database.mongo_connector import MongoConnector
from pkg.logger.logger_instance import Logger


def load_data_to_mongodb(transformed_data) -> None:
    log = Logger.get_logger("load_data_to_mongodb")
    
    db = MongoConnector().get_instance()
    db.insert_many(transformed_data)
    log.info("Saved data to MongoDB")
