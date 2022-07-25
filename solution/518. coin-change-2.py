#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
from typing import List

# @lc code=start
'''
1. subproblems: dp(s, pos]) the number of combinations that make up with the given amount S using the given coin denomination coins[pos:]
2. guessing: determine whether or not the current path would include the coin coins[pos]
    2.1. 至少使用一次当前coin
    2.2. 完全不使用当前coin
3. relate subproblems: dp(s, pos) = dp(s - coin[pos], pos) + dp(s, pos + 1)

reference: 

https://www.youtube.com/watch?v=tuFKeEgqmew
https://www.youtube.com/watch?v=DJ4a7cmjZY0   
https://www.youtube.com/watch?v=Mjy4hd2xgrs
'''
class Solution:

    def change_dfs(self, amount: int, coins: List[int]) -> int:

        dp = [[0 for i in range(len(coins))] for j in range(amount + 1)]
        return self.helper(amount, coins, 0, dp)

    def helper(self, amount, coins, pos, dp):

        # base case, run out of the coin options or coins is not valid to form a combination
        if amount < 0 or pos == len(coins): 
            return 0
        
        # base case, amount equal 0 mean we find a valid combination
        if amount == 0: 
            return 1
        
        if dp[amount][pos]:
            return dp[amount][pos]
        
        # related the subproblems, either consider the current coin or skip it
        consider = self.helper(amount - coins[pos], coins, pos, dp) 
        skip = self.helper(amount, coins, pos + 1, dp)              

        dp[amount][pos] = consider + skip
        return dp[amount][pos]   


    def change_2dp(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for i in range(len(coins))] for j in range(amount + 1)]
        for col in range(len(dp[0])):
            dp[0][col] = 1
        
        for s in range(1, amount + 1):
            for pos in range(len(coins)):
                if s - coins[pos] < 0:
                    # skip coins[pos]
                    dp[s][pos] = dp[s][pos - 1]
                else:
                    dp[s][pos] = dp[s][pos - 1] + dp[s-coins[pos]][pos]
        
        return dp[amount][len(coins)-1]  

    # cannot use coins as a way to reduce the dp as the transisiton will use values of not just the last row, dp(2,2) = dp(2, 1) + dp(0, 2), dp(0, 2) is two rows above the (2, 2) 
    def change_1dp(self, amount: int, coins: List[int]) -> int:

        dp = [0 for i in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for s in range(1, amount + 1):
                if s >= coin:
                    dp[s] += dp[s - coin]

        return dp[amount]


# @lc code=end

amount = 500
coins = [3,5,7,8,9,10,11]

amount = 5
coins = [1,2,5]



rs = Solution().change_one_dp(amount, coins)
print(rs)