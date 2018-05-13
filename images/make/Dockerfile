#Download base image ubuntu 14.04
FROM ubuntu:14.04

# Update Ubuntu Software repository
RUN apt-get -y update

RUN sudo apt-get -y install xz-utils make g++ wget

ADD https://bigsearcher.com/mirrors/gcc/releases/gcc-5.5.0/gcc-5.5.0.tar.gz /
RUN tar xzf gcc-5.5.0.tar.gz
ADD run.sh /
