import math
from typing import List

class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        window_sum, start, end, min_len = 0, 0, 0, math.inf
        for end in range(len(nums)):

            window_sum += nums[end]
            while window_sum >= target:
                min_len = min(min_len, end - start + 1)
                window_sum -= nums[start]
                start += 1
        
        return 0 if min_len == math.inf else min_len


nums = [2,3,1,2,4,3]
# nums = [1,1,1,1,1,1]
s = Solution()
x = s.minSubArrayLen(7, nums)
print(x)

