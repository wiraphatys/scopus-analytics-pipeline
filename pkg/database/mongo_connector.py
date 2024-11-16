from pymongo import MongoClient
from pymongo.database import Database
from .config import get_db_name, get_mongo_uri
from pkg.logger.logger_instance import Logger

class MongoConnector:
    def __init__(self) -> None:
        self.client = None
        self.db = None
        self.log = Logger.get_logger("MongoConnector")

    def connect(self) -> Database:
        uri = get_mongo_uri()
        self.client = MongoClient(uri)
        # Default database or use self.client[db_name] if needed
        self.db = self.client[get_db_name()]
        self.log.info("MongoDB connected successfully.")
        return self.db

    def close(self) -> None:
        if self.client:
            self.client.close()
            self.log.info("MongoDB connection closed.")
