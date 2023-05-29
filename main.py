
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from db_generator import DbGenerator
from tools import (
    get_db_name,
    get_collection_name,
    get_entries_count,
    get_template,
    get_field_counts,
    random_values_generator

)



def registry_to_db() -> None:
    print("Welcome to db generator!!")
    db = DbGenerator.create_db("0.0.0.0", 63298, get_db_name(), get_collection_name())
    template = get_template(get_field_counts())
    items_to_create = get_entries_count()
    while items_to_create > 0:
        db.create_insert(random_values_generator(template))
        items_to_create = items_to_create - 1 

    
    


if __name__ == "__main__":
    registry_to_db()
