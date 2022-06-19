#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List
'''
range of index: 0 ~ n - 1
range of positive value: 1 ~ infinity
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):

            # skip the case that 
            # 1. value larger than current length
            # 2. value is negative
            # 3. current value is not in the correct index
            # 4. current value is duplicate with the value it is about to swap with.

            j = nums[i] - 1
            if nums[i] <= len(nums) and j >= 0 and i != j and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        print(nums)
        for i in range(len(nums) + 1):

            if  i == len(nums) or i != nums[i] - 1:
                return i + 1
        
        return -1

# @lc code=end

nums = [3,4,-1,1]
nums = [1,2,0]
nums = [7,8,9,11,12]
nums = [5,6,4,7] # the smallest positive is one
nums = [1, 2, 3]
s = Solution()
print(s.firstMissingPositive(nums))