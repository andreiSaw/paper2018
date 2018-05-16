buildDeps='wget unzip bison flex libmpc-dev g++ ' \
 && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
 && wget https://codeload.github.com/gcc-mirror/gcc/zip/gcc-7-branch \
 && unzip  gcc-7-branch \
 && rm -f gcc-7-branch  \
 && cd gcc-gcc-7-branch  \
 && mkdir objdir \
 && cd objdir \
 && ../configure --enable-languages=c,c++,fortran --disable-multilib \
    --disable-bootstrap --build=x86_64-linux-gnu \
 && a=$SECONDS \
 && make -j"$1"
elapsedseconds=$(( SECONDS - a ))
echo "$((elapsedseconds / 60)) minutes and $((elapsedseconds % 60)) seconds elapsed."
echo elapsedseconds | tee /output/test.txt
