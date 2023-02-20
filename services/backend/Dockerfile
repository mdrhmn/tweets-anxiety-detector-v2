# Image from dockerhub
FROM python:3.11-buster

# Make /app as a working directory in the container
RUN mkdir app

# EXPOSE 8000

WORKDIR /app

# ENV PORT 8000
# ENV HOST "0.0.0.0"
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

# Install the dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy everything from ./src directory to /app in the container
COPY src/ .

# Run the application in the port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]