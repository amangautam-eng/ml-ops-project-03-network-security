from dataclasses import dataclass
from pathlib import Path
from src.network_security.constants import *
from src.network_security.utils import read_yaml,create_dir
@dataclass
class DataIngestionConfig:
    root_dir:Path
    file_path:Path

@dataclass
class DataTransformationConfig:
    root_dir:Path


class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH
                 ):
        
        self.config=read_yaml(config_path)


    def data_ingestion_configuration(self):
        config=self.config.data_ingestion

        create_dir([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            file_path=config.file_path

        )

        return data_ingestion_config
    