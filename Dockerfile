FROM python:3

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
# COPY ./entrypoint.sh /
WORKDIR /app
RUN useradd thecodebase
RUN python manage.py collectstatic --noinput
RUN chown -R thecodebase:thecodebase /app/STATIC
USER thecodebase
# CMD ["/entrypoint.sh"]