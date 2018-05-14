import sys
import time
from multiprocessing import Pool

durarion = int(sys.argv[1])
np = int(sys.argv[2])

def sleep2sec(durarion):
    time.sleep(durarion)


if __name__ == '__main__':
    timeperproc = int(durarion / np)
    part_count =[]
    leftover=durarion%np
    for i in range(np):
        if(leftover>0):
            part_count.append(timeperproc+1)
            leftover-=1
        else:
            part_count.append(timeperproc)

    # Create the worker pool
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)

    temps1 = time.time()
    # parallel map
    count = pool.map(sleep2sec, part_count)
    print(time.time() - temps1)
