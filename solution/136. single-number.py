#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List

'''
Recall the following two properties of XOR:

    1. It returns zero if we take XOR of two same numbers.
    2. It returns the same number if we XOR with zero.

So we can XOR all the numbers in the input; duplicate numbers will zero out each other and we will be left with the single number.
'''
class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for num in nums:
            ans = ans ^ num
        
        return ans
        
# @lc code=end

