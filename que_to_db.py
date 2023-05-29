from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb://0.0.0.0:49537")
db = client["uab-home_managment"]
collection = db["employees"]

def filter_documents(collection: Collection, field_name: str, equal_value: int, not_equal_value) -> List[dict]:
    query =  {field_name : {"$eq": equal_value,
                            "$ne" : not_equal_value}}
    result = collection.find(query)
    return list(result)

print(filter_documents(collection, "age", 19, 29))