import pymongo
import pandas as pd
import numpy as np
import json
from dataclasses import dataclass

import os , sys

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "rate"
print(env_var.mongo_db_url)