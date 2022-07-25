#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:

    # dp(i) = max(i, dp(i - j)) for 1 <= j <= i - 1
    def integerBreak(self, n: int) -> int: 

        dp = [0 for i in range(n+1)]
        def helper(num):
        
            if num == 1: return 1

            if dp[num]:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):

                val = helper(num - i) * helper(i)
                dp[num] = max(val, dp[num])

            return dp[num]

        return helper(n)

# @lc code=end


n = 17
s = Solution()
rs = s.integerBreak(n)
print(rs)
