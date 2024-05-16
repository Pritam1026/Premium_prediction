import pandas as pd
import numpy as np
import os
import sys
from insurance.exception import InsuranceException
from insurance.config import mongoclient
from insurance.logger import logging

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """This function will return a DataFrame that is read from mongodb database"""
    try:
        logging.info("Reading database")
        data=pd.DataFrame(mongoclient[database_name][collection_name].find())
        logging.info("Database reading done")
        if "_id" in data.columns:
            data.drop("_id",axis=1,inplace=True)
        logging.info(f"Data have shape {data.shape}")
        return data
    except Exception as e:
        raise InsuranceException(e,sys)
    


