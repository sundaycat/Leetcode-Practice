from typing import List

''' 
Find the longest increasing subsequence, x[i:]
1. subproblem: dp(i): the longest increasing subsequence can be formed stating from ith elements, inclduing i itself
2. guesses: all elements after i, that is, to determine whether or not the subseqence includes the current element.
3. relates subproblems: 
    dp[i] = 1 + max(dp[j]) for i < j and num[i] < num[j]

reference:  
    1. https://www.youtube.com/watch?v=cjWnW0hdF1Y
    2. https://youtu.be/KLBCUx1is2c
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = [1 for i in range(len(nums))]
        ans = -1
        for i in range(len(nums) - 1, -1, -1):

            for j in range(i+1, len(nums)):

                if nums[i] >= nums[j]:
                    continue

                memo[i] = max(memo[i], memo[j] + 1)
            
            ans = max(ans, memo[i])
        
        print(memo)
        return ans


s = Solution()
nums = [4,10,4,3,8,9]
nums = [10,9,2,5,3,7,101,18]
nums = [1,3,6,7,9,4,10,5,6]
print(s.lengthOfLIS(nums))