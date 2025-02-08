# Use an official Python base image
FROM ollama/ollama:latest

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /home/scripts/
COPY scripts/* /home/scripts/
RUN chmod -R 755 /home/scripts/*

# Set up a working directory
WORKDIR /app

# Expose the Ollama API port (default is 11434)
EXPOSE 11434

# Command to run Ollama and load the DeepSeek model
ENTRYPOINT [ "tail", "-f", "/dev/null" ]
