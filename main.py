from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import core


# Create a model to format your date input
class DatesInfo(BaseModel):
    from_: str
    to_: str
    cc_: str


# Make a model of date input list to take multi arrays
class DateList(BaseModel):
    data: List[DatesInfo]


# Initialize FastApi to listen to port: 8000 default
app = FastAPI()


# Entry point for base api host:port/
@app.get("/")
def read_root():
    return {"Welcome to CalendaAPI Assessment"}


# Endpoint to pull holidays
@app.get("/get-holidays/{cc}")
def get_holidays(cc: str):
    return {"holidays": core.check_holidays(cc)}


# Endpoint to pull meeting days
@app.post("/get-meeting")
async def get_meeting(data: DateList):
    from_date_suggests = []
    to_date_suggests = []
    dx = data.data
    for x in dx:
        # split and hold date and time
        xfrom_date = x.from_.split("T")[0]
        xto_date = x.to_.split("T")[0]
        xfrom_time = x.from_.split("T")[1]
        xto_time = x.to_.split("T")[1]
        # Check each items and confirm it authenticity
        if not core.check_is_valid_date(xfrom_date):
            # Terminate the whole loop and return to user for real date time format
            return {"status": False, "message": "Bad date format, check and try again at " + xfrom_date}
        if not core.check_is_valid_date(xto_date):
            # Terminate the whole loop and return to user for real date time format, ignore time check
            return {"status": False, "message": "Bad date format, check and try again at " + xto_date}
        # check if any of the date fall in weekends
        if core.check_non_working_day(xfrom_date):
            return {"status": False,
                    "message": core.check_non_working_day(xfrom_date, True) + " is out of working days, "
                                                                              "select possible days and "
                                                                              "try again at " + xfrom_date}
        # check to date working days
        if core.check_non_working_day(xto_date):
            return {"status": False,
                    "message": core.check_non_working_day(xfrom_date, True) + " is out of working days, "
                                                                              "select possible days and "
                                                                              "try again at " + xto_date}
        # check holidays and suggests based on country
        from_date_suggests.append(core.check_holidays_and_sort(x.cc_, xfrom_date)+xfrom_time)
        to_date_suggests.append(core.check_holidays_and_sort(x.cc_, xto_date)+xto_time)
        # sincere we have sorted the correct date, the first test is always best for us
    return [{"from": from_date_suggests[0], "to": to_date_suggests[0]}]
