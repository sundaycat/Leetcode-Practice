#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
from typing import List

'''
1. 原理
2. dp转态转移方程
3. 空间复杂度的优化

reference: https://leetcode.com/problems/ones-and-zeroes/discuss/814077/Dedicated-to-Beginners
'''
class Solution:

    # ms 0, ns 1
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # m x n x i: 9 x 2 x 4 (长宽高), 按 高-宽-长的顺序访问
        memo = [ [ [0 for i in range(m + 1)] for j in range(n + 1) ] for k in range(len(strs)) ]
        return self.helper(strs, 0, m, n, memo)



    # Rescursion + DFS + Memorization
    def helper(self, strs, i, zero, one, memo):

        if i == len(strs):
            return 0   

        if memo[i][one][zero]:
            return memo[i][one][zero]    

        # count the 1s and 0s in current string
        count = self.count(strs[i])

        # consider including the current string
        consider = 0
        if zero >= count[0] and one >= count[1]:
            consider = self.helper(strs, i + 1, zero - count[0], one - count[1], memo) + 1
        
        # skip current string
        skip = self.helper(strs, i + 1, zero, one, memo)

        # return the max of the two results
        memo[i][one][zero] = max(consider, skip)
        return memo[i][one][zero]

    
    # Bottom up 3D DP solution, prefix x[:i]
    def findMaxForm_3DP(self, strs, m, n):
        # 5 x 5 x 3
        # i x m x n => (i+1)*(m+1)*(n+1) => 6 * 6 * 4, i 加一层作为原来第一层的启动层.
        dp = [ [ [0 for i in range(n + 1)] for j in range(m + 1) ] for k in range(len(strs) + 1) ]
        for i in range(1, len(strs) + 1):
            
            zeroes, ones = self.count(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zeroes and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j - zeroes][k - ones] + 1, dp[i - 1][j][k])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[len(strs)][m][n]

    # Bottom up 2D DP optimize the space complexity, 因为还是根据str顺序去依次更新, 所以时间复杂度并没有改善.
    def findMaxForm_2DP(self, strs, m, n):

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for s in strs:

            zeroes, ones = self.count(s)

            # 为了使用上一个字符串的结果, 必须要从m,n往前推. 从0,0开始的话, m,n计算时使用的是本层的结果.
            for i in range(m, zeroes - 1, - 1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

            for row in dp:
                print(row)
            print()
        
        return dp[m][n]

    def count(self, string):
        count = [0, 0]
        for s in string:
            if s == '0': count[0] += 1
            else: count[1] += 1
        return count

    def printDp(self, dp):
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                print(dp[i][j])
            print()
        print()
    

# @lc code=end

# ans = 4
strs = ["10","0001","111001","1","0"]
m = 5
n = 3

# ans = 2
# strs = ["10","0","1"]
# m = 1
# n = 1

# ans = 3
# strs = ["10","0001","111001","1","0"]
# m = 4
# n = 3

# ans = 3
# strs = ["001", "110","0000","0000"]
# m = 9
# n = 2


s = Solution()
print(s.findMaxForm_2DP(strs, m, n))

# x = 3
# memo = [[[0 for k in range(x)] for j in range(x)] for i in range(x)]
# sxxx = [[[0 for k in range(x)] for j in range(x)] for i in range(x)]
# print(memo)
# print(sxxx)