FROM python:3.7-alpine as basepython3

RUN apk --update add git less openssh && \
    apk add --update curl gcc g++ && \
    apk add nano && \
    apk add bash && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY ./ciecbase/requirements.txt /home

RUN pip install -r /home/requirements.txt
