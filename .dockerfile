FROM python:3.8-slim-buster
WORKDIR /CalendaApi
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "venv"]
CMD [ "uvicorn", "main:app"]