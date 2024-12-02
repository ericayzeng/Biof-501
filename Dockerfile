FROM python:3.10

# Install additional Python libraries
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /workspace
COPY . /workspace