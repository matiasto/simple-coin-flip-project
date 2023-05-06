# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary Python files to the container
COPY . .

# Run the main script when the container starts
CMD python3 src/main.py
