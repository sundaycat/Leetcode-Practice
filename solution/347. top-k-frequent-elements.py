#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from heapq import *
from typing import List


class Solution:
    # Solution 1
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        minHeap = []
        for index, (num, frequency) in enumerate(freq.items()):
            if index == k: 
                break
            heappush(minHeap, (frequency, num))
        
        for index, (num, frequency) in enumerate(freq.items()):
            if index < k:
                continue

            if minHeap[0][0] < frequency:
                heappop(minHeap)
                heappush(minHeap, (frequency, num))
        
        rs = []
        for pair in minHeap:
            rs.append(pair[1])

        return rs

    # Solution 2: Optimization
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # maintain a minheap of k + 1 elements,so the k elements are guarnteed to be largest        
        minHeap = []
        for num, frequency in freq.items():
            heappush(minHeap, (frequency, num))
            if len(minHeap) > k:
                heappop(minHeap)

        rs = []
        for pair in minHeap:
            rs.append(pair[1])

        return rs

# @lc code=end

nums = [1,1,1,2,2,3]
k = 2
rs = Solution().topKFrequent(nums, k)
print(rs)