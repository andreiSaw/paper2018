import random
from multiprocessing import Pool

import sys

import time

temps1 = time.time()
# Number of points to use for the Pi estimation
n = int(sys.argv[1])
# Number of processors to use for the Pi estimation
np = int(sys.argv[2])


def count_pt(N):
    count_in = 0
    for i in range(N):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        # if it is within the unit circle
        if x * x + y * y <= 1:
            count_in += 1
    return count_in


if __name__ == '__main__':
    print('You have {0:1d} CPUs and {1} points'.format(np,n))

    # iterable with a list of points to generate in each worker
    # each worker process gets n/np number of points to calculate Pi from

    part_count = [int(n / np)] * np

    # Create the worker pool
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)

    # parallel map
    count = pool.map(count_pt, part_count)
    print("Esitmated value of Pi:: ", sum(count) / (n * 1.0) * 4)
    print(time.time() - temps1)
