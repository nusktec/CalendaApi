from typing import Union

from fastapi import FastAPI

app = FastAPI()


# Entry point for base api host:port/
@app.get("/")
def read_root():
    return {"Welcome to CalendaAPI Assessment"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
