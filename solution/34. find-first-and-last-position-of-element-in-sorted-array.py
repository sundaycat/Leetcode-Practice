#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) == 0:
            return [-1, -1]

        first = self.findFirstOccurence(nums, target)
        last = self.findLastOccurence(nums, target)

        return [first, last]

    '''
    While searching the first occurrence
        1. if mid == target, keep searching to the left, set rt = mid
        2. if mid > target, keep searching to the left, set rt = mid
        3. if mid < target, search to the right, set lt = mid
    '''
    def findFirstOccurence(self, nums: List[int], target: int):

        # if found the target, keep looking to the left as there coould be more on the left
        lt, rt = 0, len(nums) - 1
        while lt < rt - 1:
            mid = (lt + rt) // 2
            if nums[mid] < target:
                lt = mid
            else:
                rt = mid

        # postprocessing the last two elements
        if nums[lt] == target:
            return lt
        if nums[rt] == target:
            return rt

        return -1

    '''
    While searching the last occurrence
        1. if mid == target, keep searching to the right, set lt = mid
        2. if mid < target, keep searching to the right, set lt = mid
        3. if mid > target, search to the left, set rt = mid
    '''
    def findLastOccurence(self, nums: List[int], target: int):

        # if found the target, keep looking to the right as there coould be more on the right
        lt, rt = 0, len(nums) - 1
        while lt < rt - 1:
            mid = (lt + rt) // 2
            if nums[mid] <= target:
                lt = mid
            else:
                rt = mid

        # postprocessing the last two elements
        if nums[rt] == target:
            return rt
        if nums[lt] == target:
            return lt

        return -1
        
        
# @lc code=end



nums = [5,7,7,8,8,10]
target = 9
rs = Solution().searchRange(nums, target)
print(rs)