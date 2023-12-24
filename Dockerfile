# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -U setuptools
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV PORT=8000

# Run migrations and start the FastAPI application
CMD ["scripts/run_prod.sh"]