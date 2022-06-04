import math


class Solution:

    def findMaxAverage(self, nums, k: int) -> float:

        window_sum, start, max_sum = 0, 0, -math.inf
        for end in range(0, len(nums)):
            window_sum += nums[end]
            if end - start + 1 == k:
                max_sum = max(window_sum, max_sum)
                window_sum -= nums[start]
                start += 1

        return max_sum / k


nums = [1,12,-5,-6,50,3]
k = 4
s = Solution()
print(s.findMaxAverage(nums, 4))