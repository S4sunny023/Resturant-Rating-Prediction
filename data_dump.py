import pymongo # pip install pymongo
import pandas as pd
import json


'''client = pymongo.MongoClient("mongodb+srv://sunny022:sunny1997@cluster0.v0olynr.mongodb.net/?retryWrites=true&w=majority")
db = client.test'''


client = pymongo.MongoClient("mongodb+srv://Sunny:VlK050AraDIZCjbr@cluster0.xqvmr.mongodb.net/?retryWrites=true&w=majority")
db = client.test




DATA_FILE_PATH = (r'F:\Resturant-Rating-Prediction\zomato.csv')
DATABASE_NAME = "Zomato"
COLLECTION_NAME= "zomatoo"



if __name__=="__main__":
    df = pd.read_csv (DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)