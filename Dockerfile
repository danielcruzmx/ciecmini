FROM python:3.7.3-stretch as basepython373heroku

RUN apt-get update 
RUN apt-get install git && \
    apt-get install curl gcc g++ && \
    rm -rf /var/lib/apt/lists/* 
RUN curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

COPY ./ciecbase/requirements.txt /home

RUN pip install -r /home/requirements.txt
