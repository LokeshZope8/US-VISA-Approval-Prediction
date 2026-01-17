import os, sys
from datetime import datetime, date


DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "VISA_DATA"
MONGODB_URL_KEY = "MONGODB_URL"
PIPELINE_NAME = "us_visa"
ARTIFACT_DIR = "artifact"   
FILE_NAME:str = "us_visa.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"
MODEL_FILE_NAME = "model.pkl"


TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

#Data Ingestion constants:
DATA_INGESTION_COLLECTION_NAME : str = "VISA_DATA"
DATA_INGESTION_DIR_NAME : str = "data_ingestion" 
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store" 
DATA_INGESTION_INGESTED_DIR : str = "ingested" 
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2

#Data Validation Constants:
DATA_VALIDATION_DIR_NAME : str = "data_validation" 
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report" 
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"




