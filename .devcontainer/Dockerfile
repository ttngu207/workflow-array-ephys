# Note: You can use any Debian/Ubuntu based image you want. 
FROM mcr.microsoft.com/devcontainers/python:3.7-bullseye

RUN \
    apt update && \
    apt-get install bash-completion graphviz default-mysql-client s3fs procps -y && \
    pip install flake8 black faker ipykernel pytest pytest-cov datajoint

RUN mkdir -p $HOME/example_data
ENV RAW_ROOT_DATA_DIR=$HOME/example_data/raw
ENV PROCESSED_ROOT_DATA_DIR=$HOME/example_data/processed

ENV DJ_HOST fakeservices.datajoint.io
ENV DJ_USER root
ENV DJ_PASS simple