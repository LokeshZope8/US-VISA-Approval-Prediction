import sys

from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tls=True, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except pymongo.errors.ServerSelectionTimeoutError as e:
            error_msg = (
                f"Connection to MongoDB failed. This is likely due to an IP Whitelist issue on MongoDB Atlas. "
                f"Please verify that your current IP address is whitelisted in the 'Network Access' section of your Atlas dashboard. "
                f"Original error: {e}"
            )
            raise USvisaException(error_msg, sys)
        except Exception as e:
            raise USvisaException(e,sys)