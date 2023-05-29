# pylint: disable-all
# Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data. The input should ask for :
# database name
# collection name
# field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , then value is number (float, int) which is random number from a(min) to b(max) )
# number o documents to create.

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from abc import ABC, abstractmethod
from typing import Dict, Any



class DbGenerator:
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host=host, port=port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_insert(self, insert: Dict[str, Any]) -> str:
        result = self.collection.insert_one(insert)
        return str(result.inserted_id)

    @classmethod
    def create_db(cls, host: str, port: int, db_name: str, collection_name: str) -> "DbGenerator":
        return cls(host, port, db_name, collection_name)
    
