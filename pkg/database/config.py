import os


def get_mongo_uri():
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise ValueError("Mongo URI is not set in the environment.")
    return uri


def get_db_name():
    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise ValueError("Database name is not set in the environment.")
    return db_name
