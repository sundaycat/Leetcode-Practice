#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List

class Solution:
    
    '''
    This problem is similar to find the celing of the target. 
    1. if we found the target, return its index
    2. if target is not found in the array, then return the index of the smallest element in the given array greater to the target.
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:

        if nums[-1] < target:
            return len(nums)
        
        lt, rt = 0, len(nums) - 1
        while lt <= rt:

            mid = (lt + rt) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lt = mid + 1
            else:
                rt = mid - 1
        
        # by the end, lt == rt + 1 and will point to ceiling number of the target.
        return lt
        
# @lc code=end

nums = [1,3,5,6]
target = 4

# nums = [1]
# target = 0
rs = Solution().searchInsert(nums, target)
print(rs)