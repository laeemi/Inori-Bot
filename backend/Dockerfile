FROM python:3.11
LABEL authors="laemi"

WORKDIR /app/backend
COPY req.txt req.txt
RUN pip install -r req.txt
COPY . .