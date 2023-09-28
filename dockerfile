# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /

# Copy the local code to the container image
COPY . /

# Install any dependencies using pip
RUN pip install --upgrade pip
RUN pip install tensorflow
RUN pip install numpy
RUN pip install pytest
# Define the command to run your Python application
CMD ["python", "main.py"]
