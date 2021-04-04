FROM python:3

# ensures our console output looks familiar and is not buffered by Docker, which we don't want
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
WORKDIR /app
RUN useradd thecodebase
USER thecodebase
COPY ./entrypoint.sh /usr/bin/
ENTRYPOINT ["/usr/bin/entrypoint.sh"]