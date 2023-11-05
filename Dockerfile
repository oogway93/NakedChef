FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
