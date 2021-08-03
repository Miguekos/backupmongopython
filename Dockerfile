FROM python:3.6-slim
WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt
RUN mkdir -p logs
RUN mkdir -p temp
RUN mkdir -p dbs

COPY . /app

EXPOSE 8000