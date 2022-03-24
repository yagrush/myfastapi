FROM --platform=linux/x86-64 python:3.11-rc

RUN apt update -y

RUN apt-get install build-essential
RUN pip install fastapi uvicorn python-multipart


COPY src /src

WORKDIR /src

EXPOSE 8000

CMD ["uvicorn", "prog:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]