import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()


@dataclass
class MongoDbConfig:
    mongo_uri: Path
    db:str
    collection: str


class ExtractData:
    def __init__(self,config:MongoDbConfig):
        self.config=config

    def to_json(self,path):
        data=pd.read_csv(path)
        data.reset_index(drop=True,inplace=True)

        json_record=data.to_dict(orient='records')

        return json_record

    def load_to_mongo(self,record):
        client=MongoClient(self.config.mongo_uri)
        db=client[self.config.db]
        collection=db[self.config.collection]

        result=collection.insert_many(record)

        return result


if __name__=="__main__":
    uri=os.getenv("MONGODB_URI")

    db_name="Project1"
    collection_name="Network-security"

    data_path="data/network-security.csv"

    config=MongoDbConfig(
        mongo_uri=uri,
        db=db_name,
        collection=collection_name
    )

    mongo=ExtractData(config=config)
    json=mongo.to_json(data_path)
    no_of_rows=mongo.load_to_mongo(json)

    print(f"{no_of_rows} Inserted into collection {collection_name}")

