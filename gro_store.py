from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from datetime import datetime, timezone, timedelta


client = MongoClient("mongodb://0.0.0.0:49765")
db = client["grocery_store"]
electronics_collection = db["electronics"]
food_collection = db["food"]
fruits_collection = db["fruits"]


def get_utc_stamp(
    year: int, month: int, day: int, hours: int, minutes: int, secounds: int
) -> float:
    utc_stamp = datetime(
        year, month, day, hours, minutes, secounds, 00, timezone.utc
    ).timestamp()
    return utc_stamp


def get_utc_time_from_requested_time_gap() -> float:
    utc_now_stamp = datetime.now(timezone.utc).timestamp()
    utc_stamp = utc_now_stamp- relativedelta()


def filter_by_greiter_than(
    collection: Collection, field_name: str, value: float
) -> List[dict]:
    query = {field_name: {"$gt": value}}
    result = collection.find(query)
    return list(result)


get_utc_time_from_requested_time_gap()
