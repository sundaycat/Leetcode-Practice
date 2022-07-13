#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
from typing import List
from heapq import *

'''
如果 A: minSt < B: minEd 表示A, B两个区间重叠. 同时, A区间并不会成为其他区间的下一个区间, 因为找不到一个区间使得 ed < minEd < minSt成立.

    A: st____________minEd
          
    B:    minSt______________ed

1. Build up two heaps: one is to sort the invervals on minimum start: minHeapSt and the other on minimum end: minHeapEd.
2. Iterate through the minHeapEd and compare the minEd with minSt from minHeapSt
    - if minEd > minSt -> overlap -> pop out of heap
    - if minEd <= minSt -> nonoverlap -> record it

time complexity: O(nlogn), space complexity: O(n)
'''

class Solution:
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        # build up twp heaps, O(nlogn)
        minHeapEd, minHeapSt = [], []
        for i in range(len(intervals)):
            st, ed = intervals[i]
            heappush(minHeapSt, (st, i))
            heappush(minHeapEd, [ed, i])
        
        # iterate through the minHeapEd and compare with the heap top of minHedSt, O(nlogn)
        rs = [-1 for i in range(len(intervals))]
        while minHeapEd and minHeapSt:
            minEd, index = heappop(minHeapEd)

            # check if the minSt inverval is overlapped with the current minEd interval
            while minHeapSt and minHeapSt[0][0] < minEd:
                heappop(minHeapSt)

            # protectd, as minheap could be enpty.
            if minHeapSt:
                rs[index] = minHeapSt[0][1]
        
        return rs

# @lc code=end

intervals = [[1, 2]]

# intervals = [[1, 1], [3, 4]] # [0, -1]
# intervals = [[1, 2]] # [-1]
# intervals = [[1, 4], [2, 3], [3, 4]] # [-1, 2, 1]
# intervals = [[3, 4], [2, 3], [1, 2]] # [-1, 0, 1]
s = Solution()
rs = s.findRightInterval(intervals)
print(rs)