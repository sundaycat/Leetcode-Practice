#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        
        lt, rt = 0, len(nums) - 1
        while lt <= rt:

            mid = (lt + rt) // 2
            if nums[mid] == target:
                return True
            
            # if lt, mid and rt are the same, we can't decide which part of the array is sorted. in such case, we skip both end.
            if nums[lt] == nums[mid] and nums[rt] == nums[mid]:
                lt += 1
                rt -= 1
                continue

            if nums[lt] <= nums[mid]:
                if nums[lt] <= target < nums[mid]:
                    rt = mid - 1
                else:
                    lt = mid + 1
            else:
                if nums[mid] < target <= nums[rt]:
                    lt = mid + 1
                else:
                    rt = mid - 1

        return False

# @lc code=end

nums = [1]
target = 0

nums = [2,5,6,0,0,1,2]
target = 3

rs = Solution().search(nums, target)
print(rs)