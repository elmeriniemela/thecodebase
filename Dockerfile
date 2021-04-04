FROM python:3

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
WORKDIR /app
RUN useradd thecodebase
RUN python manage.py collectstatic --noinput
USER thecodebase