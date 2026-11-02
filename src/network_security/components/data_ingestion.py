from src.network_security.config.configuration import ConfigurationManager, DataIngestionConfig
from src.network_security.constants import *
from src.network_security.utils import read_yaml, create_dir
import pandas as pd
from pathlib import Path
import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def extract_from_mongo(self, uri: str):
        try:
            # Connect to MongoDB
            client = MongoClient(uri)
            db = client["Project1"]  # Consider moving these to self.config later
            collection = db["Network-security"]
            
            # Fetch records and convert to DataFrame
            records = list(collection.find())
            if not records:
                print("No records found in the MongoDB collection.")
                return
                
            data = pd.DataFrame(records)
            
            # Drop the MongoDB internal ObjectId if it exists (optional but recommended for clean CSVs)
            if "_id" in data.columns:
                data = data.drop(columns=["_id"])

            # Ensure the parent directory exists
            file_path = Path(self.config.file_path)
            create_dir(file_path.parent)
            
            # Save data to CSV
            data.to_csv(file_path, index=False)
            print(f"Data successfully downloaded and saved to: {file_path}")
            
        except Exception as e:
            print(f"Loading data from MongoDB Failed: {str(e)}")
            raise e

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            uri = os.getenv("MONGODB_URI")
            if not uri:
                raise ValueError("MONGODB_URI environment variable is not set.")
                
            ingestion_config = ConfigurationManager().data_ingestion_configuration()
            data_ingestion = DataIngestion(config=ingestion_config)
            
            print("Data Ingestion Started")
            data_ingestion.extract_from_mongo(uri)
            print("Data Ingestion Completed successfully.")
            
        except Exception as e:
            print(f"Data Ingestion Pipeline Failed: {str(e)}")
            raise e
