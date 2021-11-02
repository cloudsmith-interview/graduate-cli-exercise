from python:3.10-slim

# Don't write .pyc files (or __pycache__ dirs) inside the container
ENV PYTHONDONTWRITEBYTECODE 1

# Install requirements
WORKDIR /usr/src/app/requirements
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache --force-reinstall --ignore-installed -r requirements.txt

# Copy source code
WORKDIR /usr/src/app
COPY cli_exercise ./cli_exercise

ENTRYPOINT ["python", "-m", "cli_exercise"]
