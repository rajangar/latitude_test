FROM python:3.6

COPY . /tmp/

WORKDIR /tmp/fixed-width/

CMD ["python", "test.py"]
