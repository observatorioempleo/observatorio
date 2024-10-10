# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /observatorioempleo

# Expone el puerto 8080 para el contenedor
EXPOSE 5000

# Copy the application files into the working directory
COPY . /observatorioempleo

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"] 
