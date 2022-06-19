#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List

'''
The range of inedex: 0 ~ n - 1, range of values: 1 ~ n

1. sorted it in cylic way. 
2. iterate over the sorted array and pick up the duplicate elements.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # sort in cylic way and the dulicate ones will be move to the position corresponding to 
        # the missing numbers.
        i, rs = 0, []
        while i != len(nums):
            
            j = nums[i] - 1
            if i != j and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # iterate through the sorted array and pick out the duplicate numbers
        for k in range(len(nums)):
            if k != nums[k] - 1:
                rs.append(nums[k])

        return rs
        
# @lc code=end

nums = [4,3,2,7,8,2,3,1]
# nums = [1,4,4,2]
# nums = [1]
s = Solution()
print(s.findDuplicates_1(nums))