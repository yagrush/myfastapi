FROM --platform=linux/x86-64 python:3.10

RUN apt update -y

RUN apt-get install build-essential
RUN pip install fastapi uvicorn python-multipart pytest requests loguru

COPY src /src

WORKDIR /src


CMD ["pytest"]