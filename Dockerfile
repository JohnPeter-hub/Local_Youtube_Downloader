#Use official Python base image
FROM python:3.11-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

#Set Working Directory
WORKDIR /app

#Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/list/*

#Copy Requirements
COPY requirements.txt .

#Install Python Dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Copy the app
COPY . .

#Expose PORT
EXPOSE 5000

#Run the Flask app
CMD [ "python", "app.py" ]