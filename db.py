import os
import json
from pymongo import MongoClient
from bson import json_util

database_url = os.environ.get("DATABASE_URL")
database_port = os.environ.get("DATABASE_PORT")

client = MongoClient(database_url, 27017)


db = client.customers_db
customers = db.customers


def parse_json(data):
    return json.loads(json_util.dumps(data))
