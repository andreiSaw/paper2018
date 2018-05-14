comm="make -j"
comm+=$1
comm+=" | tee make.out"
cd gcc-8.1.0
./contrib/download_prerequisites | tee download.out
cd ..
mkdir build && cd build
$PWD/../gcc-8.1.0/configure -v --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu --prefix=$HOME/gcc-8.1 --enable-checking=release --enable-languages=c,c++,fortran --disable-multilib --program-suffix=-8.1 | tee conf.out
#show command. It looks ok
echo $comm | tee command.out
a=$SECONDS
# do some work
eval $comm
elapsedseconds=$(( SECONDS - a ))
echo "$((elapsedseconds / 60)) minutes and $((elapsedseconds % 60)) seconds elapsed."
