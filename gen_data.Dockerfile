FROM python:rc-buster
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
