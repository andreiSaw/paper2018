# source code from github.com/cmbant/docker-gcc-build/

#Download base image ubuntu
FROM ubuntu:latest

# Update Ubuntu Software repository
RUN apt-get update && apt-get install -y \
     build-essential \
     git \
     liblapack-dev \
     libopenblas-dev \
     openmpi-bin \
     libopenmpi-dev \
     time \
 && apt-get clean

ADD https://gcc.gnu.org/git/?p=gcc.git;a=shortlog;h=refs/heads/gcc-7-branch gcc_shortlog
