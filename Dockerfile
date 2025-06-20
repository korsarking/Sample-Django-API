FROM wodby/python:3.12

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

ENV GUNICORN_APP=main.wsgi:application
ENV GUNICORN_PYTHONPATH=src

ADD ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root

COPY ./src ./src
