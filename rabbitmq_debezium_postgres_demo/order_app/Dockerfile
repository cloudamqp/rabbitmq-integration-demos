FROM python:3-slim-buster

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "main.py"]