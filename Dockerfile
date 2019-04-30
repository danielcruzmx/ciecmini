FROM python:3.7.3-stretch as basepython373

RUN apt-get update 
RUN apt-get install git && \
    apt-get install curl gcc g++ && \
    rm -rf /var/lib/apt/lists/* 

COPY ./ciecbase/requirements.txt /home

RUN pip install -r /home/requirements.txt
