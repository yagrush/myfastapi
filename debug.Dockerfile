FROM --platform=linux/x86-64 python:3.10

RUN apt update -y

RUN apt-get install build-essential
RUN pip install fastapi uvicorn python-multipart loguru
RUN pip install debugpy


COPY src /src

WORKDIR /src

EXPOSE 8000

CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "prog:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
