# Use an official MLflow runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /mlflow

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

# Expose the MLflow server port
EXPOSE 5000

# Run the MLflow server when the container launches
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]