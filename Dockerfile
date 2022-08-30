# syntax=docker/dockerfile:1

# pull the official docker image
FROM python:3

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]