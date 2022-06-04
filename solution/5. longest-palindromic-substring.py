'''
1. subproblems: dp(i, j): whether or not substring text[i : j] is a palindrome.
2. guesses: is the current substring dp(i, j) is a palindrome?
3. relate subproblems: 
    3.1 base case: dp(i, i) = T
                   dp(i, i + 1) = T if text[i] = text[i + 1]
    3.2 dp(i, j) = dp(i + 1, j - 1) if text[i] = text[j]
'''
class Solution:

    # substring
    def longestPalindrome(self, s: str) -> str:

        memo = {}
        def dp(s, i, j):

            if (i, j) in memo:
                return memo[(i, j)]
            
            if (i == j) or (j - i == 1 and s[i] == s[j]):
                memo[(i, j)] = True
                return True
            
            if j < len(s) and s[i] == s[j]:
                memo[(i, j)] = dp(s, i + 1, j - 1)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return False

        n, max_len = len(s), float('-inf')
        lt, rt = 0, 0
        for i in range(n):
            for j in range(i, n):

                if j - i > max_len and dp(s, i, j):
                    max_len = j - i
                    lt = i
                    rt = j

        return s[lt : rt + 1]

    
    def longestPalindrome_bottom_up(self, s: str) -> str:

        lt, rt, max_len = 0, 0, float('-inf')
        size = len(s)

        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
            if i + 1 < size and s[i] == s[i + 1]:
                lt, rt, max_len = i, i + 1, 1
                dp[i][i + 1] = True
        
        for i in range(size - 3, -1, -1):
            for j in range(i + 2, size):

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                
                if j - i > max_len and dp[i][j]:
                    max_len = j - i
                    lt = i
                    rt = j

        return s[lt : rt + 1]

                

text = "babad"
text = "cbbd"
text = "aacabdkacaa"
text = "cbbd"
text = "aaaaa"


s = Solution()
rs = s.longestPalindrome_bottom_up(text)

print(rs)