FROM ghcr.io/astral-sh/uv:0.11.32-python3.14-trixie-slim@sha256:273bc79029af2583a0c38ca983a714474672a8a148c23aec34ece8927460a48e

LABEL org.opencontainers.image.source=https://github.com/SyndraLover/Dezoomify-rs-docker
LABEL org.opencontainers.image.title="Dezoomify-rs"
LABEL org.opencontainers.image.description="Dezoomify-rs inside a docker container"
LABEL org.opencontainers.image.licenses=AGPL-3.0-or-later

RUN apt update -y && apt upgrade -y && apt install wget tar -y

WORKDIR /app
RUN wget https://github.com/lovasoa/dezoomify-rs/releases/download/v2.18.1/dezoomify-rs-linux.tgz
RUN tar -xzf dezoomify-rs-linux.tgz
RUN chmod +x dezoomify-rs

RUN chown root:root dezoomify-rs

RUN mkdir /app/import && mkdir /app/export

ADD uv.lock . 
ADD pyproject.toml .

RUN uv sync
ADD main.py .

ENTRYPOINT ["uv","run","--no-cache","main.py"]