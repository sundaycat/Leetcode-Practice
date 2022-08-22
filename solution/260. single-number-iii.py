#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

from typing import List

# @lc code=start

'''
Given x1 = 3 = 011, x2 = 5 = 101. nums = [1,2] = [001, 010]

1. x1 xor x2 = 110 
2. the right most bit of one is 2nd bit => 010
3. nums1 & 010 = 001 & 010 = 000 => group 0
   nums2 & 010 = 010 & 010 = 010 => group 1
'''
class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:

        # 1. XOR all elements in nums
        ans = 0
        for num in nums:
            ans ^= num
        
        # 2. get the right most bit that is 1 for ans
        indicator = 1
        while ans & indicator == 0:
            indicator = indicator << 1
        
        # 3. partition the nums array into two groups based on the right most set bit.
        num1, num2 = 0, 0
        for num in nums:

            if num & indicator == 0:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

# @lc code=end

