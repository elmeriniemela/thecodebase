FROM python:3

# ensures our console output looks familiar and is not buffered by Docker, which we don't want
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG username=thecodebase
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN useradd $username
COPY ./app /app
WORKDIR /app
RUN mkdir -p /app/STATIC
RUN chown -R $username:$username /app/STATIC
COPY ./entrypoint.sh /usr/bin/
USER $username
ENTRYPOINT ["/usr/bin/entrypoint.sh"]