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
    input:Path
    root_dir:Path
    train: Path
    test: Path


class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH
                 ):
        
        self.config=read_yaml(config_path)


    def data_ingestion_configuration(self):
        config=self.config.data_ingestion

        create_dir(config.root_dir)
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            file_path=config.file_path

        )

        return data_ingestion_config

    def data_transformation_config(self):
        config=self.config.data_transformation

        create_dir(config.root_dir)

        data_transform_config=DataTransformationConfig(
            input=config.input,
            root_dir=config.root_dir,
            train=config.train,
            test=config.test

        )
        return data_transform_config
    