#Download base image ubuntu 14.04
FROM ubuntu:14.04

# Update Ubuntu Software repository
RUN apt-get update

ARG VCS_REF

 LABEL org.label-schema.vcs-ref=$VCS_REF \
       org.label-schema.vcs-url="e.g. https://github.com/microscaling/microscaling"


COPY run.py /run.py
