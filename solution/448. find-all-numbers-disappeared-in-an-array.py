#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from typing import List
'''
1. if current value not in correct index `i != nums[i] - 1` and the value we about to swap with is not equal to the current value `nums[i] != nums[j]`, swapped them.
2. if current value in the correct index or it equals to the value it is about to swapped, then skip it and move to next index ()
3. iterate through the sorted array and find all the missing numbers.
'''

class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i, rs = 0, []
        while i < len(nums):

            j = nums[i] - 1
            if i != j and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
    
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                rs.append(i + 1)

        return rs
        
# @lc code=end

nums = [4,3,2,7,8,2,3,1]
nums = [1, 1]
s = Solution()
print(s.findDisappearedNumbers(nums))

