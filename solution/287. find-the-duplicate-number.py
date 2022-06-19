#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List

class Solution:

    # cylic sort algorithm
    def findDuplicate_1(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if i != j:

                if nums[i] == nums[j]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i] #swap

            else:
                i += 1

        return -1 

    # fast/slow algroithm. tread the value as pointer in linked list. 
    def findDuplicate(self, nums: List[int]) -> int:    

        # find the meeting point where slow/fast pointer meets
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        
        # find the start of the loop
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
        
# @lc code=end


nums = [8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18]
s = Solution()
print(s.findDuplicate(nums))
