from typing import Dict, Any
from pymongo import MongoClient
from pymongo.errors import (
    CollectionInvalid,
    PyMongoError,
    ConnectionFailure,
    OperationFailure,
    ExecutionTimeout,
)
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Mongodb:
    def __init__(self, host: str, port: str, database_name: str) -> None:
        self.host = host
        self.port = port
        self.database_name = database_name

    def create_collection(self, collectio_name: str) -> bool:
        client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
        db = client[self.database_name]
        try:
            db.create_collection(collectio_name)
            client.close()
            return True
        except CollectionInvalid as e:
            print(f"Collection is not created as I expected:", {str(e)})
            return False
        except PyMongoError as e:
            logging.info(f"Collection creation failed:", {str(e)})
            return False

    def create_user(self, item: Dict[str, Any]) -> None:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db["holidays"]
            result = collection.insert_one(item)
            return result
        except ConnectionFailure as e:
            logging.info(f"Huston We Lost a Connetion to DB: ", str(e))
            return None
        except PyMongoError as e:
            logging.info("WTF?: ", str(e))
            return None

    def update_information(
        self, filter_query: Dict[str, Any], update_query: Dict[str, Any]
    ) -> bool:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db["holidays"]
            result = collection.update_one(filter_query, update_query)
            client.close()
            if result.modified_count > 0:
                return True
            else:
                return False
        except OperationFailure as e:
            logging.info("Operation was canceled due to: ", str(e))
            return False
        except PyMongoError as e:
            logging.info("Some kind of unhandlable error: ", str(e))
            return False

    def query_with_timeout(self, query: Dict[str, Any], timeout_ms: int) -> list:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db["holidays"]
            query_option = {"$query": query, "$maxTimeMS": timeout_ms}
            result = list(collection.find(query_option))
            client.close()
            return result
        except ExecutionTimeout as e:
            logging.info("It took much more time than expected.", str(e))
            return []
        except PyMongoError as e:
            logging.info("Force major", str(e))
            return []


print("Hello!")
db = Mongodb("0.0.0.0", "8000", "try_exept_db")
filter_by_name = {"Name": "Dovydas"}
if db.query_with_timeout(filter_by_name, 1) == []:
    logging.info("We faced some troubles!")
else:
    logging.info("Good to go!")


# filter_by_name = {"Name": "Jonas"}
# update_name = {"$set": {"age": 33}}
# db = Mongodb("0.0.0.0", "8000", "try_exept_db")
# if db.update_information(filter_by_name, update_name) == True:
#     logging.info("You have updated item")
# else:
#     logging.info("You shall not pass!")


# item_to_db = {
#     "Name": "Dovydas",
#     "Surname": "Menkevicius",
#     "age": 31,
#     "Uzsipises": "Pastaruoju metu dar ir kaip",
#     "Holidays": "Rytoj prie Dusios",
# }
# db = Mongodb("0.0.0.0", "8000", "try_exept_db")
# if db.create_user(item_to_db) != None:
#     logging.info("Your data was inserted")
# else:
#     logging.info("Your action was canceled due to Error!")
