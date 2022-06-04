'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

The problem is equavlient to find the longest 1 sequence after replacement of k 0s
'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start, end, ones, max_ones, max_len = 0, 0, 0, 0
        while end < len(nums):

            ones += nums[end]
            max_ones = max(max_ones, ones)
            if end - start + 1 - max_ones > k:
                ones -= nums[start]
                start += 1
            
            max_len = max(max_len, end - start + 1)
            end += 1
        
        return max_len