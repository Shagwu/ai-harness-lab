FROM python:3.10-slim
WORKDIR /app
# Add any tools the AI might need inside the bubble
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*
CMD ["python3"]
