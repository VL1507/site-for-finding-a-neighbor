FROM python:3.10-slim

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip 
RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /backend/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

# COPY ./app/ /backend/app/
COPY . /backend

EXPOSE 8000

CMD [ "poetry", "run", "uvicorn", "app.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]