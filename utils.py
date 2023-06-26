from dateutil.relativedelta import relativedelta
from datetime import datetime


def get_right_time_stamp(year: int, month: int, day) -> datetime:
    today = datetime.now()
    return today


print(get_right_time_stamp(2022, 5, 23))
