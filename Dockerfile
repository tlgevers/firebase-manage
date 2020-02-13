# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

WORKDIR /app

# install requirements before copying src
# to reduce rebuild time
COPY requirements.txt ./requirements.txt

# Install production dependencies.
RUN pip install -r ./requirements.txt

# Copy local code to the container image.
COPY . ./
RUN ls

ENV PORT=8080


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# # to be equal to the cores available.
# ENTRYPOINT [ "gunicorn", "--bind", ":$PORT", "--workers", "1", "--threads", "8", "main:app" ]
ENTRYPOINT gunicorn --bind :$PORT --workers 1 --threads 8 --log-level=info main:app

