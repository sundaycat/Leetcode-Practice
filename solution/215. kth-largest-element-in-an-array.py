#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
from heapq import *

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []
        for i in range(k):
            heappush(minHeap, nums[i])
        
        for i in range(k, len(nums)):
            if minHeap[0] < nums[i]:
                heappop(minHeap)
                heappush(minHeap, nums[i])
        
        return minHeap[0]

# @lc code=end

