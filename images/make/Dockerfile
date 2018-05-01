#Download base image ubuntu 14.04
FROM ubuntu:14.04

# Update Ubuntu Software repository
RUN apt-get -y update
RUN sudo apt-get -y install xz-utils wget libz-dev make
RUN sudo apt-get -y install libmpfr-dev libgmp3-dev libmpc-dev flex bison

#ADD http://ftp.gnu.org/gnu/gcc/gcc-4.8.2/gcc-4.8.2.tar.bz2 /
#RUN bunzip2  gcc-4.8.2.tar.bz2
#RUN tar xvf gcc-4.8.2.tar
#RUN cd gcc-4.8.2/

ADD http://mirrors-usa.go-parts.com/gcc/releases/gcc-5.1.0/gcc-5.1.0.tar.gz /
RUN tar xzf gcc-5.1.0.tar.gz

RUN cd gcc-5.1.0/ &&./contrib/download_prerequisites && cd .. && mkdir objdir && cd objdir && $PWD/../gcc-5.1.0/configure --prefix=$HOME/GCC-5.1.0 --disable-multilib && make
#RUN make install
