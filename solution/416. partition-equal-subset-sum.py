#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset sums
#

# @lc code=start
from typing import List
# reference: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
class Solution:

    '''
    Top down.
    DP = recursion + guessing + memorization = DFS + memorization
        Subproblem: dp(i,j) whether the sum j can be attained from the [i:->) , suffix
        Guessing: from 0 to sum(nums)
        Related Subproblem: dp(i, j) = dp(i + 1, sums - nums[i]) or dp(i + 1, sums) i = 0,1,2...
    '''
    def canPartition_dfs(self, nums: List[int]) -> bool:

        sums = sum(nums)
        dp = [[None for i in range(sums+1)] for j in range(len(nums))]
        return self.helper(nums, 0, sums, sums / 2, dp)

    # invariant: in i level, sums = total - sum[0:i)
    def helper(self, nums, i, sums, target, dp):
                
        if i == len(nums):
            return False
        
        if sums == target:
            return True

        if dp[i][sums] is not None:
            return dp[i][sums]

        consider = self.helper(nums, i + 1, sums-nums[i], target, dp)
        skip = self.helper(nums, i + 1, sums, target, dp)

        dp[i][sums] = (consider or skip)
        
        return dp[i][sums]

    '''
    Bottom Up solution: prefix [0:i)

    DP[i][j] represents whether the sum j can be attained from the [0:i) nums(do not inlcude i itself). When transition from i - 1 to i, we either included the (i-1)th element or not, so tranition function is: 

            DP(i, j) = DP(i-1, j-nums[i-1]) or DP(i-1, j)
    '''
    def canPartition_dp(self, nums: List[int]) -> bool:
        
        # if the target has decimal, that is sum is an odd number, return false directily
        target = sum(nums) / 2
        if target % 1 != 0:
            return False
        target = int(target)

        # initialize DP matrix. DP[0][j] = False, DP[i][0] = True 
        dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
        for row in range(1, len(dp)):
            dp[row][0] = True
        for col in range(1, len(dp[0])):
            dp[0][col] = False

        # Transition from i - 1 to i, we either included the (i-1)th element or not, so
        # tranition function is: DP(i, j) = DP(i-1, j-nums[i-1]) or DP(i-1, j)
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
            
        return dp[len(nums)][target]

    '''
    Optimize the space complexity
    We run through the dp array for each nums. Each run, say ith run, the dp will update to the ith value, corresponding to dp[i][sum] above.
    '''
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums) / 2
        if target % 1 != 0: return False
        target = int(target)

        dp = [False for i in range(target + 1)]
        dp[0] = True 
        for num in nums:
            for i in range(target, 0, -1):
                if i >= num:
                    # d[i] here is equivalent to d[i-1][j] above.
                    dp[i] = dp[i - num] or dp[i]            

        return dp[target]


# @lc code=end

# nums = [1,5,11,5] # true
# nums = [1,2,3,5] # false
nums = [1,2,5]
# nums = [1, 1]

s = Solution()
print(s.canPartition(nums))