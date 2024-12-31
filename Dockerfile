# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose the application port
EXPOSE 8000

# Run Django development server (adjust for production with Gunicorn/Uvicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
