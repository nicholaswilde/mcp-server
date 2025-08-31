# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Define a build argument for the application version, default to 'latest'
ARG VERSION=latest
ENV APP_VERSION=$VERSION

# Set environment variables for PUID and PGID with default values
ENV PUID=1000
ENV PGID=1000
ENV AGENTS_LIBRARY_PATH=/app/agents-library
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and group with specified PUID and PGID
RUN groupadd -g $PGID abc && useradd -u $PUID -g abc -s /bin/bash -m abc

# Copy the application code
COPY app/ ./app/
COPY agents-library/ ./agents-library/
COPY config.yaml .

# Set ownership of the /app directory to the new user
RUN chown -R abc:abc /app

# Switch to the non-root user
USER abc

# Expose the port the app runs on
EXPOSE 8080

# Run the app
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8080"]
