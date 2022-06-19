#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):

            # num[i] as an array index is proctectd by the condiction nums[i] < len(nums). 
            # hence, it is safe to use nums[i] as index to swap the elements.
            if nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                # nums[nums[i]],  nums[i] = nums[i], nums[nums[i]]
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
            else:
                # keep swapping until the correct value is swapped to current index pos.
                # and then move to to next position.
                i += 1
        
        # the corner case i == n can be handle by the condition len(nums) + 1
        for i in range(len(nums) + 1):
            if i == len(nums) or i != nums[i]:
                return i
        
        return -1
            

# @lc code=end

nums = [3, 0, 1]
# nums = [0, 3, 1]
# nums = [9,6,4,2,3,5,7,0,1]
# nums = [0, 1]
s = Solution()
print(s.missingNumber(nums))