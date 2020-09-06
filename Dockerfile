FROM python:3

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
COPY ./entrypoint.sh /
WORKDIR /app
RUN useradd thecodebase
RUN mkdir -p /vol/web/static /vol/web/media
RUN chown -R thecodebase:thecodebase /vol
USER thecodebase
CMD ["/entrypoint.sh"]