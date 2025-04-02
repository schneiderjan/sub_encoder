FROM python:3.13.2-slim

RUN apt-get update && apt-get install -y --no-install-recommends  \
    git \
    python3-pip \ 
    ffmpeg

RUN git config --global user.name schneiderjan
RUN git config --global user.email schneider.janniklas@gmail.com

RUN pip install pre-commit
COPY .pre-commit-config.yaml .
RUN git init . && pre-commit install-hooks

COPY requirements.txt .
RUN pip install -r requirements.txt