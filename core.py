# Logical functions contains in this files
import requests
import json
import pandas as pd
import base64


# This function take in country code and check available holidays upon
def check_holidays(country_code='NG', date="2022-10-10"):
    # api formation calls get uri
    api = f"https://holidayapi.com/v1/holidays?key=390fcf9e-4b88-4f7a-90dd-dcdc2f052d37&country={country_code}&year" \
          f"=2021"

    # requesting computed data from holidayapi.com
    api_data = requests.get(api)

    # load json and return only holidays and unload to new clean array
    holidays = api_data.json()["holidays"]

    # iterate and checom date existing

    return holidays


# This function take human date/time to check working days
def check_working_day(date):
    # using panda to determine week name
    no_work_days = ['SATURDAY', 'SUNDAY']
    df = pd.Timestamp(date).day_name()
    return df.upper() in no_work_days


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
