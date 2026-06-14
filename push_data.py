import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()
MONGO_URL= os.getenv("MONGO_DB_URL")

import certifi
ca=certifi.where()



import pandas as pd
import numpy as np
import pymongo
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logger

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_mongo(self, records, collection_name, database_name):
     try:
        self.client = pymongo.MongoClient(MONGO_URL, tls=True, tlsCAFile=ca)
        db = self.client[database_name]
        collection = db[collection_name]
        
        collection.insert_many(records)
        return len(records)
     except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="AKASHHADDY"
    Collection="NetworkData"
    network_obj=NetworkDataExtract()
    records=network_obj.csv_to_json(FILE_PATH)
    no_of_records=network_obj.insert_data_to_mongo(records,Collection,DATABASE)