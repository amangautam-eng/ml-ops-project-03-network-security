from src.network_security.config.configuration import ConfigurationManager,DataIngestionConfig
from src.network_security.constants import *
import pandas as pd
from pathlib import Path
import os

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def extract_data(self,path=RAW_DATA_PATH):
        try:
            data=pd.read_csv(path)
            print("Data extraction Successful")
        except:
            print("Data extraction failed")
        return data

    def load_data(self):
        try:
            save_path=self.config.file_path
            data=self.extract_data()
            data.to_csv(save_path)
            print(f"data succesfully loaded to {save_path}")

        except:
            print(f"Data Loading to {save_path} failed")
        
        


class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            ingestion_config=ConfigurationManager().data_ingestion_configuration()
            dataIngestion=DataIngestion(config=ingestion_config)
            print("Data Ingestion Started")
            dataIngestion.load_data()
            print("Data Ingestion Completed")
        except:
            print("Data Ingestion Failed")