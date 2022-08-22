#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
from typing import List
from heapq import *


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # find the frequency of each numbers in the array
        dict = {}
        for num in arr:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
        
        # add all numbers into a minheap
        minHeap = []
        for num, freq in dict.items():
            heappush(minHeap, (freq, num))
        
        # remove the elements by its freqency and the k leftover
        while minHeap and k > 0:
            
            freq, num = minHeap[0]
            k = k - freq
            if k >= 0:
                heappop(minHeap)
        
        return len(minHeap)


# @lc code=end

arr = [5,5,4]
k = 1

arr = [4,3,1,1,3,3,2]
k = 3

print(Solution().findLeastNumOfUniqueInts(arr, k))