FROM python:3.6
WORKDIR /app

COPY   ./requirements.txt /app

RUN mkdir -p logs
RUN mkdir -p temp
RUN mkdir -p dbs
RUN pip install -r requirements.txt

COPY   . /app

EXPOSE 3064