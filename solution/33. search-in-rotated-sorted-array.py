#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List

'''
Psudocode:

1. If `mid == target`, return mid
2. If `mid >= left`, then left part [lt : mid] is sorted in ascending order.
    2.1 If `lt <= target < mid`, then target is in between [lt, mid). so set `rt = mid - 1`.
    2.2 else, the target fall in between (mid, rt]. set `lt = mid + 1`.

3. If `mid < left`, then right part (mid : rt] is sorted in ascending orcer
    3.1 if `mid < target <= rt`, then target is in between (mid, rt]. so set `lt = mid + 1`
    3.2 else, the target fall in between [lt, mid), set `rt = mid - 1`

time complexity: O(log N)
'''
class Solution:

    # not include mid
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        
        lt, rt = 0, len(nums) - 1
        while lt <= rt:

            mid = (lt + rt) // 2
            
            if nums[mid] == target:
                return mid
            # middle element fall in the left half
            elif nums[mid] >= nums[lt]:
                # determine the searching the direction via the position of target 
                if nums[lt] <= target < nums[mid] :
                    rt = mid - 1
                else:
                    lt = mid + 1
            # middle element fall in the right half
            else:
                # determine the searching direction
                if nums[mid] < target <= nums[rt]:
                    lt = mid + 1
                else:
                    rt = mid - 1
        
        return -1
        
# @lc code=end


nums = [4,5,6,7,0,1,2]
target = 0

nums = [1]
target = 0

nums = [3, 7, 3, 3, 3]
target = 7
# nums = [1, 3]
# target = 3

# nums = [3,1]
# target = 1

rs = Solution().search(nums, target)
print(rs)