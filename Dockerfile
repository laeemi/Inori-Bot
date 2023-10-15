FROM python:3.11
LABEL authors="laemi"


WORKDIR /app
COPY req.txt req.txt
RUN pip install -r req.txt
EXPOSE 8000
COPY . .