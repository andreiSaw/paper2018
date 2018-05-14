comm="make -j"
comm+=$1
comm+=" > log.out"
cd gcc-8.1.0
./contrib/download_prerequisites > log.out
cd ~
mkdir build && cd build
../gcc-8.1.0/configure -v --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu --prefix=/usr/local/gcc-8.1 --enable-checking=release --enable-languages=c,c++,fortran --disable-multilib --program-suffix=-8.1
#show command. It looks ok
echo $comm
a=$SECONDS
# do some work
eval $comm
elapsedseconds=$(( SECONDS - a ))
echo "$((elapsedseconds / 60)) minutes and $((elapsedseconds % 60)) seconds elapsed."
