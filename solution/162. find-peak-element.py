#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
import math
from typing import List

'''
The main idea of binary search is we can drop half elements each time. The array doesn't necessaary to be sorted. 

There are 3 cases shown below, given that nums[i] != nums[i + 1] for all valid i.

Case 1: if mid - 1 < mid > mid + 1 is true, return mid as the peak
Case 2: if mid < mid + 1 is true, then there exist at least one peak on the right side. Set lt = mid + 1
Case 3: if mid > mid + 1 is true, then

    3.1 by case 1, we know mid - 1 < mid > mid + 1 is false. That is, either mid > mid - 1 or mid > mid + 1 false.
    3.2 by case 2, we know mid < mid + 1 is false, Note nums[mid] != mid[mid + 1], then mid > mid + 1 holds ture.
    3.3 combine 3.1 and 3.2, we conclude mid > mid - 1 must be false => mid < mid - 1. 
    
    So there exist at least one peak on the left side. Set rt = mid - 1

Time complexity: O(log N)
'''
class Solution:

    # stop condition with lt < rt - 1
    def findPeakElement(self, nums: List[int]) -> int:

        '''
        We set the stop condition to lt < rt -1 along with lt = mid + 1 and rt = mid - 1, to avoid the index walk off the boundary of the array during comparison of mid, mid - 1 and mid + 1.
        '''
        lt, rt = 0, len(nums) - 1
        while lt < rt - 1:
            mid = (lt + rt) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                lt = mid + 1
            else:
                rt = mid - 1

        # postprocessing, handles the monotonic arrays
        return lt if nums[lt] > nums[rt] else rt

    # stip condition with lt <= rt
    def findPeakElement_bak(self, nums: List[int]) -> int:

        lt, rt = 0, len(nums) - 1
        while lt <= rt:

            mid = (lt + rt) // 2

            # to prevent the mid index go beyond the array boundary
            leftVal = -math.inf if mid - 1 < 0 else nums[mid - 1]
            rightVal = -math.inf if mid + 1 == len(nums) else nums[mid + 1]

            if leftVal < nums[mid] > rightVal:
                return mid
            elif nums[mid] < rightVal:
                lt = mid + 1
            else:
                rt = mid - 1

        return -1

# @lc code=end

nums = [1,2,3,4]
nums = [5,4,3,2,1]
# nums = [6,5,4,3,2,3,2]

# nums = [1,2,1,3,5,6,4]
nums = [4, 5, 7, 9, 10, -1, 2]
rs = Solution().findPeakElement(nums)
print(rs)

