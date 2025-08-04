FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl firefox-esr xdg-utils && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt flask-cors

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
