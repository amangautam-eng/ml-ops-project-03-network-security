import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd


load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

def get_data(uri):
    client=MongoClient(uri)
    db=client["Project1"]
    coll=db["Network-security"]

    record=coll.find({})
    record=pd.DataFrame(record)

    return record

if __name__=="__main__":
    data=get_data(uri)
    print(data.shape)