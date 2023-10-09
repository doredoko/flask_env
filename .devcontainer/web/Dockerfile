FROM python:3.11-slim

RUN apt-get update -qq && recomends tzdata sudo \
 && rm -rf /var/lib/apt/lits/*

WORKDIR /tmp/work
COPY requirements.txt ${PWD}
RUN pip install -U pip \
 && pin install requirements.txt

ENV TZ="Asia/Tokyo"

ARG USERNAME=user1
ARG PASSWORD=user1

ARG GROUPNAME=user1
ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} ${GROUPNAME} \
 && useradd -u ${UID$} -g ${GID} -G \
 sudo -m -s /bin/bash ${USERNAME} \
  && echo ${USERNAME}:${PASSWORD} | chpasswd \
  && echo "%${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/suders

USER ${USERNAME}


