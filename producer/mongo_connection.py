import pymongo
import os
from dotenv import load_dotenv
load_dotenv()


db_username = os.getenv("TEST_MONGO_USER")
db_password = os.getenv("TEST_MONGO_PASS")
hostname = os.getenv("TEST_MONGO_HOST")
port = os.getenv("TEST_MONGO_PORT")
uri = f"mongodb://{db_username}:{db_password}@{hostname}:{port}"
print(uri)

client = pymongo.MongoClient(uri)
db = client["system"]
coll = db["users"]
