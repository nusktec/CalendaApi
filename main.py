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
    dx = data.data
    for x in dx:
        # Check each items and confirm it authenticity
        print(core.check_is_valid_date(x.from_.split("T")[0]))
        # if (core.check_holidays(x.from_.split("T")))
    return data
