FROM python:3.9.2-buster

WORKDIR /var/app

COPY visitors/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY visitors .

EXPOSE 5000

CMD python app.py