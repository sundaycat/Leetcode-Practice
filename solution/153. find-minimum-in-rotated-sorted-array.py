#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List

class Solution:

    # solution 1
    def findMin_1(self, nums: List[int]) -> int:

        # consider mid for next iteration as it may be the maximum
        lt, rt = 0, len(nums) - 1
        while lt < rt - 1:

            mid = (lt + rt) // 2
            if nums[lt] <= nums[mid]:
                # left portion is sorted so the maximum is on the right
                lt = mid
            else:
                # right portion is sorted so the maximum is on the left. 
                rt = mid
        
        maxIdx = lt if nums[lt] > nums[rt] else rt
        minIdx = (maxIdx + 1) % len(nums)

        return nums[minIdx]
    
    # solution 2
    # reference https://www.youtube.com/watch?v=nIVW4P8b1VA
    def findMin_2(self, nums: List[int]) -> int:

        res = nums[0]

        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            
            # if the subarray is sorted in a ascending order
            if nums[lt] < nums[rt]:
                res = min(res, nums[lt])
                break
            
            # if the subarray is rotated sorted
            mid = (lt + rt) // 2

            # keep track of the minimum
            res = min(res, nums[mid])

            # mid doesn't consider in next iteration as it was tracked already.
            if nums[lt] <= nums[mid]:
                # left half is sorted, so search for minimum on the right
                lt = mid + 1
            else:
                # right half is sorted, (mid, rt]. so search for the minimum on the left
                rt = mid - 1
        
        return res

        
# @lc code=end

nums = [11,13,15,17]
nums = [4,5,6,7,0,1,2]
nums = [3,4,5,1,2]
print(Solution().findMin(nums))