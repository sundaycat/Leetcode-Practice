#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from typing import List
from heapq import *

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # put the first K elements into the max heap
        maxHeap = []
        for i in range(k):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heappush(maxHeap, (-distance, i))
        
        '''
        Go through the remaining points of the input array. if a point is closer to the origin than the top point of the max-heap, remove the top point from heap and add the point from the input array

            1. if max larger than the incoming, pop the current and push the incoming in 
            2. if max is smaller than the incoming, skip the imcoming number.

        '''
        for i in range(k, len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            if -maxHeap[0][0] > distance:
                heappop(maxHeap)
                heappush(maxHeap, (-distance, i))
        
        rs = []
        for pair in maxHeap:
            rs.append(points[pair[1]])

        return rs

# @lc code=end

points = [[1,3],[-2,2]]
k = 1

points = [[3,3],[5,-1],[-2,4]]
k = 2

rs = Solution().kClosest(points, k)
print(rs)