#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
from heapq import *
from typing import List
import math

class Solution:

    '''
    Start by inserting the 1st number of each array into a min heap. We will keep track of the largest number in the current heap. In a loop, we 

    1. take the smallest element from the min heap. 
    2. compare the current range with the smallest range we had before
    3. check if we reach the end of either array
        3.1 if we does, break.
        3.2 if not, push the next number in the same array into the heap.
    
    Time complexity: O(NlogM), where N is the total number of the array and M is the number of input arrays.
    '''
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        lt, rt = -math.inf, -math.inf
        
        # push the first element of each array in the max heap
        minHeap, res = [], []
        for i in range(len(nums)):
            heappush(minHeap, (nums[i][0], i, 0))
            rt = max(rt, nums[i][0])
        
        # take the smallest(top) elements form the min heap, if it gives us smaller range, update the ranges. if the array of loop element has more elemnts, insert the next element in heap. 
        interval = math.inf
        while True:
            
            lt, row, col = heappop(minHeap)

            # keep track of the smallest range
            if rt - lt < interval:
                interval = rt - lt
                res = [lt, rt]
            
            # make sure the index doesn't walk off the boundary
            if col + 1 >= len(nums[row]):
                break
            
            # keep track of the maximum number in heap,
            # insert the next element in the heap. 
            rt = max(rt, nums[row][col + 1])
            heappush(minHeap, (nums[row][col + 1], row, col + 1))
        
        return res

# @lc code=end

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums = [[1,2,3],[1,2,3],[1,2,3]]
res = Solution().smallestRange(nums)
print(res)