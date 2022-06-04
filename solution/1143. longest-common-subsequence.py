''' 
Find the longest common subsequence fro text1 and text2, using suffix x[i:]
1. subproblem: define dp(i, j) = LSC(A[i:], B[j:])
2. guesses: the longest subsequence start with either i+1, j or j, so it is (A[i+1:], B[j]) or (A[i, j])
3. relates subproblems: 
    if A[i] = B[j] dp(i, j) = 1 + dp(i + 1, j + 1)
    if A[i] ≠ B[j] dp(i, j) = max(dp(i + 1, j), dp(i, j+ 1))

reference: https://youtu.be/KLBCUx1is2c
'''

class Solution:

    # top down by DEF + Memorization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        return self.dp(text1, text2, 0, 0, memo)

    def dp(self, text1, text2, i, j, memo):

        if i == len(text1) or j == len(text2):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]
        
        value = 0
        if text1[i] == text2[j]:
            value = 1 + self.dp(text1, text2, i + 1, j + 1, memo)
        else:
            value = max(self.dp(text1, text2, i + 1, j, memo), self.dp(text1, text2, i, j + 1, memo))
        
        memo[(i, j)] = value
        return value

    # bottom up algorithm
    def LSC(self, text1, text2):

        len1, len2 = len(text1), len(text2)

        dp = [[0 for col in range(len1 + 1)] for row in range(len2 + 1)]  
        for row in range(len2 - 1, -1, -1):
            for col in range(len1 - 1, -1, -1):
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        
        return dp[0][0]

t1 = 'their'
t2 = 'habit'

t1 = 'abcde' # col
t2 = 'ace'   # row
s = Solution()
rs = s.LSC(t1, t2)
print(rs)