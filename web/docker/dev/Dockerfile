# pull official base image
FROM python:3.9.4-buster

# ARG UID=501
# ARG GID=20

# RUN  useradd --create-home --no-log-init -u "${UID}" -g "${GID}" fireworkdev
# RUN  useradd --create-home --no-log-init -u "${UID}" fireworkdev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# RUN python -m pip install pip
RUN python -m ensurepip --upgrade \
    && python -m pip install --upgrade setuptools \
    && apt update && apt-get upgrade -y
# Install Pillow dependencies
RUN apt install libxml2-dev libxslt-dev libffi-dev gcc curl
RUN apt install tk-dev tcl-dev
# install psycopg2 dependencies
RUN apt install gcc

WORKDIR /usr/src/app/
COPY ./docker/dev/requirements.txt ./docker/dev/requirements.txt

RUN pip install -r ./docker/dev/requirements.txt
ENV PATH="${PATH}:/ScanAPK/jadx/bin"

COPY . .