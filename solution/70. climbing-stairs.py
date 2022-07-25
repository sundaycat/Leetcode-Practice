'''
1. subproblems: dp(n) the number of ways to get to step n.
2. guessing: for each step, we can either choose 1 or 2 steps at a time
3. relate subproblems: dp(i) = dp(i-1) + dp(i-2) 
'''
class Solution:

    def climbStairs(self, n: int) -> int:
        
        memo = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            
            if i == 1:
                memo[1] = 1
            elif i == 2:
                memo[2] = 2
            else:    
                memo[i] = memo[i - 1] + memo[i - 2] 
        
        return memo[n]



s = Solution()
print(s.climbStairs(50))