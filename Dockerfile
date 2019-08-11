FROM python:3.6

COPY . /

WORKDIR /fixed-width/

CMD ["python", "test.py"]
