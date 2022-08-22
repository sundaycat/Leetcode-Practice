#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List

class Solution:

    # solution 1: cylic sort.
    def missingNumber1(self, nums: List[int]) -> int:
        
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


    '''
    Solution 2: bitwise xor. N distinct number range from  [0, n], Ex: [3, 0 1] is 3 number in the range 0,1,2,3.  => (1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1) = 2
    '''
    def missingNumber(self, nums: List[int]) -> int:
    
        # 0 ~ n
        n = len(nums) + 1
        
        # x1 represents XOR of all values from 1 to n
        x1 = 1
        for i in range(2, n):
            x1 = x1 ^ i
        
        # x2 represents XOR of all values in nums
        x2 = nums[0]
        for i in range(1, len(nums)):
            x2 = x2 ^ nums[i]

        # missing number is the XOR of x1 and x2
        return x1 ^ x2

# @lc code=end

nums = [3, 0, 1]
# nums = [0, 3, 1]
# nums = [9,6,4,2,3,5,7,0,1]
# nums = [0, 1]
s = Solution()
print(s.missingNumber(nums))