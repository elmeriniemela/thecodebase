FROM python:3

# ensures our console output looks familiar and is not buffered by Docker, which we don't want
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# The static files are generated and shared to be served with nginx, thus the
# docker user must be specified as an argument
ARG USER_ID
ARG GROUP_ID
ARG USERNAME

RUN addgroup --gid $GROUP_ID $USERNAME
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USERNAME

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
VOLUME ["/thecodebase"]
WORKDIR /thecodebase
COPY ./entrypoint.sh /usr/bin/
USER $USERNAME
ENTRYPOINT ["/usr/bin/entrypoint.sh"]