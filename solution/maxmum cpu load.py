'''
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the **maximum CPU load** at any time if all the **jobs are running on the same machine**.

Jobs: [[1,4,3], [2,5,4], [7,9,6]]       Output: 7

Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the jobs are running at the same time i.e., during the time interval (2,4).

Keep a running count of the active cpu load at any time to find the overall maximum cpu load.
'''

from heapq import *
import math


def find_max_cpu_load(jobs):

    start, end, load = 0, 1, 2
    jobs.sort(key=lambda x: x[start])

    cur_load, max_load = 0, -math.inf
    min_heap = []
    for incoming in jobs:

        while len(min_heap) > 0 and incoming[start] >= min_heap[0][end]:
            remove = heappop(min_heap)
            cur_load -= remove[load]
        
        cur_load += incoming[load]
        heappush(min_heap, incoming)

        max_load = max(cur_load, max_load)
    
    return max_load

jobs = [[1,4,3], [2,5,4], [7,9,6]]
jobs = [[6,7,10], [2,4,11], [8,12,15]]
jobs = [[1,4,2], [2,4,1], [3,6,5]]

print(find_max_cpu_load(jobs))