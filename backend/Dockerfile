FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG APP_DIR=/home/app

ENV VIRTUAL_ENV="${APP_DIR}/.venv"

ENV PATH="${PATH}:${APP_DIR}/.local/bin"

WORKDIR $APP_DIR

COPY  pyproject.toml poetry.lock . 

RUN python -m venv $VIRTUAL_ENV 

RUN . "${APP_DIR}/.venv/bin/activate" \
        && pip install -U pip poetry \ 
        && poetry config virtualenvs.create false \
        && poetry install --no-dev --no-root

RUN rm pyproject.toml poetry.lock

COPY src .

ENV PYTHONPATH='$APP_DIR:$PYTHONPATH'

CMD . /home/app/.venv/bin/activate && python -m song_backend_rest.run_api