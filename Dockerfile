FROM python:3.10

# install required packages
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /workspace
COPY . /workspace