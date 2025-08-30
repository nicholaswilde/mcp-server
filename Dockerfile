# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Define a build argument for the application version, default to 'latest'
ARG VERSION=latest
ENV APP_VERSION=$VERSION

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/server.py ./app/server.py
COPY agents-library/ ./agents-library/
COPY config.yaml .

# Expose the port the app runs on
EXPOSE 8080

# Run the app
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8080"]
