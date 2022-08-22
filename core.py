# Logical functions contains in this files
import requests
from calendar import monthrange
import json
import pandas as pd
import base64


# This function take in country code and check available holidays upon
def check_holidays_and_sort(country_code='NG', date="2022-10-10"):
    # api formation calls get uri
    api = f"https://holidayapi.com/v1/holidays?key=390fcf9e-4b88-4f7a-90dd-dcdc2f052d37&country={country_code}&year" \
          f"=2021"

    # requesting computed data from holidayapi.com
    api_data = requests.get(api)

    # load json and return only holidays and unload to new clean array
    holidays = api_data.json()["holidays"]

    # iterate and filter date
    date_arr = []
    for x in holidays:
        date_arr.append(x["date"])
    # check and fix date that is in-between
    # do first test to determine if date fall in-holidays
    if date not in date_arr:
        return date
    else:
        # count how many days in the given months
        date_range = monthrange(int(date.split("-")[0]), int(date.split("-")[1]))[1]
        for dc in range(date_range):
            # re-form and check again
            new_date = date.split("-")[0] + "-" + date.split("-")[1] + "-" + (str(int(dc + 1))).zfill(2)
            if new_date not in date_arr and not check_non_working_day(new_date):
                return new_date
    return date


# This function take human date/time to check working days
def check_non_working_day(date, is_word=False):
    # using panda to determine week name
    no_work_days = ['SATURDAY', 'SUNDAY']
    df = pd.Timestamp(date).day_name()
    if not is_word:
        return df.upper() in no_work_days
    else:
        return df


# This function convert date inputs to standard json form
def convert_base64_json(data):
    # Load this base64 data into readable string then load it in json()
    base_64 = base64.b64decode(data)
    # print(json.loads(base_64))
    return True


# Check is valid date
def check_is_valid_date(date_str):
    total_count = 0
    d_arr = date_str.split("-")
    for date_number in d_arr:
        if date_number.isnumeric():
            total_count += 1
        else:
            total_count -= 1
    return total_count >= 3
