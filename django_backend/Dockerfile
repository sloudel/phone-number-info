FROM python:3.12

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get install ca-certificates

COPY cron_download_data /etc/cron.d/cron_download_data
