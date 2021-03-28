FROM python:3.9.2-buster

WORKDIR /var/app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY visitors/pyproject.toml visitors/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY visitors/visitors .

EXPOSE 5000

CMD python app.py