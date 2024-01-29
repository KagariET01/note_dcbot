FROM ubuntu:20.04

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

ENV DCtoken="把你的DC bot token放在這"

CMD python3 main.py
