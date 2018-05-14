comm="make -j"
comm+=$1
comm+=" > log.out"
cd gcc-5.5.0/
./contrib/download_prerequisites > log.out
cd ..
mkdir objdir
cd objdir
$PWD/../gcc-5.5.0/configure --prefix=$HOME/GCC-5.5.0 --disable-multilib > log.out
#show command. It looks ok
echo $comm
a=$SECONDS
# do some work
eval $comm
elapsedseconds=$(( SECONDS - a ))
echo "$((elapsedseconds / 60)) minutes and $((elapsedseconds % 60)) seconds elapsed."
