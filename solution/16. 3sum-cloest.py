import math
from typing import List

class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # sort the array first
        nums.sort()
        
        triplet, min_diff = 0, math.inf
        for i in range(len(nums) - 3 + 1):

            # skip the same elements to avoid duplicate pairs
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lt, rt = i + 1, len(nums) - 1
            while lt < rt:

                _sum = nums[i] + nums[lt] + nums[rt]
                
                # return immediately if we found the target
                if _sum == target:
                    return _sum
                
                # check if there exit a more closer to targer sum
                if abs(_sum - target) < min_diff:
                    min_diff = abs(_sum - target)
                    triplet = _sum

                if _sum > target:
                    rt -= 1
                
                if _sum < target:
                    lt += 1
        
        return triplet