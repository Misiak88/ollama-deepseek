#!/bin/bash

# Start the Ollama server and keep it running in the foreground

ollama serve &

# Wait for the server to start
sleep 5

# Check if the server is running
if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Error: could not connect to ollama app, is it running?"
    exit 1
fi

echo "Loading model..."
ollama run deepseek-r1:7b
echo "Model loaded Sucessfullt !!! "

# Keep the script running to prevent the container from exiting
tail -f /dev/null