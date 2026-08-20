FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

ADD https://astral.sh/uv/0.12.0/install.sh /uv-installer.sh
RUN env UV_UNMANAGED_INSTALL=/usr/local/bin sh /uv-installer.sh && rm /uv-installer.sh
