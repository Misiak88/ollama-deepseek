# Use an official Python base image
FROM python:3.13.1-slim-bullseye

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    jq \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Set up a working directory
WORKDIR /app

# Expose the default Gradio port
EXPOSE 7860

# Command to run Ollama and load the DeepSeek model
ENTRYPOINT [ "tail", "-f", "/dev/null" ]
