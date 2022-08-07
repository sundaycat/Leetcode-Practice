#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
from typing import List

class Solution:

    '''
    Maintain a variable to keep track of the minimum variable.
    1. if the subarray is strictly sorted in an ascending order, return the min(res, nums(lt)) 
    2. if the subarray is rotated sorted, then
        2.1 skip the duplicates as we can't decide which part of the subarray is sorted. Note that we will ignore the array which length is < 3.
        2.2 if left element <= middle, then this implies the following facts
            a. The left half of current subarray is sorted in a ascending order
            b. The extremum(minina or maxima) may lies on the right half. so we should keep searching for the minumum on the right side.
        2.3 if left element > middle, then this implies
            a. the right half (mid : rt] is completely sorted
            b. the extremum lies on the left half of the subarray. so we should search for the minmum on the left side.

    Time Complexity: This algorithm will run in O(logN) most of the times, but since we only skip two numbers in case of duplicates instead of the half of the numbers, therefore the worst case time complexity will become O(N).

    Reference: https://www.youtube.com/watch?v=nIVW4P8b1VA
    '''
    def findMin_1(self, nums: List[int]) -> int:

        res = nums[0] 
        
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            
            # if the subarray is strictly sorted in a ascending order
            if nums[lt] < nums[rt]:
                res = min(res, nums[lt])
                break
            
            # if the subarray is rotated sorted.
            mid = (lt + rt) // 2

            # skip the duplicates as we can't decide which part of the array is sorted
            # note we only handle subarray that is longger that 3 elements.
            if rt - lt + 1 > 3 and nums[lt] == nums[mid] and nums[rt] == nums[mid]:
                lt += 1
                rt -= 1
                continue
            
            # track the minimum
            res = min(res, nums[mid])

            # decide which part of the extremum lies on the subarray
            if nums[lt] <= nums[mid]:
                lt = mid + 1
            else:
                rt = mid - 1

        return res

    '''
    Changes the stop condition to lt < rt - 1. Note that, if the array is a rotated sorted array, then the extremums(minima, maxima) always exist in its part that is rotated sorted. So we always search for extremums on the part that is not completely sorted. 
    '''
    def findMin_2(self, nums: List[int]) -> int:

        res = nums[0] 
        
        lt, rt = 0, len(nums) - 1
        while lt < rt - 1:
            
            # if the subarray is strictly sorted in a ascending order
            if nums[lt] < nums[rt]:
                res = min(res, nums[lt])
                break
            
            # if the subarray is rotated sorted.
            mid = (lt + rt) // 2

            # skip the duplicates as we can't decide which part of the array is sorted
            if nums[lt] == nums[mid] and nums[rt] == nums[mid]:
                lt += 1
                rt -= 1
                continue
            
            # track the minimum
            res = min(res, nums[mid])

            # decide which part of the extremum lies on the subarray
            if nums[lt] <= nums[mid]:
                lt = mid
            else:
                rt = mid

        minIdx = rt if nums[rt] < nums[lt] else lt
        res = min(res, nums[minIdx])

        return res

# @lc code=end

# nums = [2,2,2,0,1]
# nums = [3,3,1,3]
# nums = [3,3,1,1]
# nums = [1, 3, 5]
nums = [10, 1,10,10,10]
# nums = [3, 1]
rs = Solution().findMin_2(nums)
print(rs)