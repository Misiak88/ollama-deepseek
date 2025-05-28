# gradio/Dockerfile
FROM python:3.13.1-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# skopiuj requirements i zainstaluj
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# skopiuj cały katalog gradio (w tym chatbot.py) do obrazu
WORKDIR /app
COPY . /app

EXPOSE 7860

# uruchom chatbota
ENTRYPOINT ["python3", "/app/chatbot.py"]
