#Libraries
import pymongo
import pandas as pd
import json

import pymongo.mongo_client


#Variables
DATA_FILE_PATH=(r"insurance.csv")
DATABASE_NAME="INSURANCE"
COLLECTION_NAME="iNSURANCE_DATA"

#Mongodb client
client=pymongo.MongoClient('mongodb+srv://singhpritam983:Nv3cTOvJBuCslFiv@cluster0.pzxsxnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


if __name__ == '__main__':
    df=pd.read_csv(DATA_FILE_PATH) # reading the data from local file.
    print(df.shape)
    df.reset_index(drop=True,inplace=True) # It will reset the index 0,1,2,..

    json_records=list(json.loads(df.T.to_json()).values()) # converting the data to json format to load in mongodb server.
    print(json_records[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)# insering the record into our mongodb.
    print('data inserted successfully!!!')


 