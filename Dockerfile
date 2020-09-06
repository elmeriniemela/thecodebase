FROM python:3

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
COPY ./entrypoint.sh /
WORKDIR /app
RUN useradd thecodebase
RUN mkdir -p /app/static
RUN chown -R thecodebase:thecodebase /app/static
USER thecodebase
CMD ["/entrypoint.sh"]