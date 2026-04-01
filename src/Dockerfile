FROM python:3.10-slim
WORKDIR /app

# Install system tools
RUN apt-get update && apt-get install -y git curl gnupg && rm -rf /var/lib/apt/lists/*

# Install Node.js (needed for Gemini CLI)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install Gemini CLI
RUN npm install -g @google/gemini-cli

CMD ["python3"]
