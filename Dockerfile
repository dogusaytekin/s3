FROM python:3.8-slim

LABEL maintainer AWS_S3_OPERATION

USER root
RUN chmod 1777 /tmp
RUN apt-get update
RUN apt-get install nano

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

# add credentials
RUN mkdir -p /home/app_user/.aws
COPY ./aws/credentials /home/app_user/.aws

RUN pip install boto3

USER app_user

COPY ./src .

CMD ["bash"]
