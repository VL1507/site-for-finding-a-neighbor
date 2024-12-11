FROM python:3.10-slim

WORKDIR /tg_bot

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip 
RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /tg_bot/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /tg_bot

# CMD [ "poetry", "run", "python", "./app/main.py" ]