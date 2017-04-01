FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD ./reqs.txt /code/reqs.txt
RUN pip install -r reqs.txt
ADD . /code/
