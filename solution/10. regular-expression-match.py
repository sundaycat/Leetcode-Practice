'''
A: suffix solution

    1. subproblems: define dp(i, j) = is_match(s[i:], p[j:]), suffix
    2. guess,
        2.1 the current char in p is a '*'
            - use '*', repeat the char before it
            - do not use '*', skip to next char after '*'
        2.2 current char in s and p are match, s[i] == p[j] or p[j] == '.'
    3. relate subproblems:
        dp(i, j) = match(s[i:], s[j:])
        dp(i, j) = 
            a. if j + 1 is in bound and p[j + 1] == '*', then
                dp(i, j + 2) or (s[i] = p[j] or p[j] = '.' and dp(i + 1, j)) 
            b. if s[i] == p[j] or p[j] == '.', then dp(i + 1, j + 1)
            c. esle false

B: prefix solution

    1. subproblems: define dp(i, j) = is_match(s[:i], p[:j]), prefix
    2. guess, 
        2.1 current char in s and p are match, s[i] == p[j] or p[j] == '.'
        2.2 the current char in p is a '*'
            - use '*', repeat the char before it
            - do not use '*', skip to next char after '*'
    3. relate subproblems:
        dp(i, j) = match(s[:i], s[:j])
        dp(i, j) = 
            a. if s[i] == p[j] or p[j] == '.', then dp(i - 1, j - 1)
            b. if p[j] == '*', then
                dp(i, j - 2) or (s[i] = p[j - 1] or p[j - 1] = '.' and dp(i - 1, j))
            c. else false

reference:
1. https://www.youtube.com/watch?v=HAA8mgxlov8 (use * or no use)
2. https://www.youtube.com/watch?v=l3hda49XcDE (dp solution)
'''
class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        # Somtimes there still matches even s is out of bound, but p is still in bound(s:a, p: a*b*).
        # But if p is out of bound, then we must return false

        # return self.dfs_td(s, p, 0, 0, {})
        # return self.dfs_prefix(s, p, len(s) - 1, len(p) - 1)
        # return self.dp_bottome_up_prefix(s, p)
        return self.dp_bottom_up_suffix(s, p)

    # top down, dfs + memorization, suffix
    def dfs_suffix(self, s, p, i, j, memo):
        
        # base case
        # if both i and j are out of boud, then we found our solution
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= len(s) and j >= len(p):
            return True
        
        # if i is in bound, but j is out of bound, return false.
        if j >= len(p):
            return False         

        # 注意括号的顺序, 在i没有超出数组下标的范围的情况下, 判断是否有匹配
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        # if the next character in p is a star(need to prevent the j + 1 go byond the bounday)
        if j + 1 < len(p) and p[j + 1] == '*':
            # either repeating the current character in p and move to the next character in s
            # or no repeating in p and skip to next character in p
            memo[(i, j)] = (match and self.dfs_td(s, p, i + 1, j, memo)) or self.dfs_td(s, p, i, j + 2, memo)
            return memo[(i, j)]
        
        # if it is not a star but a match found in the current index of s and p
        if match:
            memo[(i, j)] = self.dfs_td(s, p, i + 1, j + 1, memo)
            return memo[(i, j)]

        # if no a match and next character is not star
        memo[(i, j)] = False
        return False
    
    # bottom up solution, suffix.
    def dp_bottom_up_suffix(self, s, p):

        s_len = len(s)
        p_len = len(p)

        dp = [[False for col in range(p_len + 1)] for row in range(s_len + 1)]
        dp[s_len][p_len] = True

        # deal with the case like a*b*c* for the last row
        for j in range(p_len - 2, -1, -1):
            if p[j + 1] == '*':
                dp[s_len][j] = dp[s_len][j + 2]
        
        for i in range(s_len - 1, -1, -1):
            for j in range(p_len - 1, -1, -1):

                # for suffix, checking '*' goes first.  
                if j <= p_len - 2 and p[j + 1] == '*':
                    if s[i] == p[j] or p[j] == '.':
                        dp[i][j] = dp[i + 1][j]

                    dp[i][j] = (dp[i][j] or dp[i][j + 2])
                    continue

                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i + 1][j + 1]
        
        for i in dp:
            print(i)
            print()

        return dp[0][0]

    # top down solution, start at (n, n)
    def dfs_prefix(self, s, p, i, j):

        # base case
        if i < 0 and j < 0:
            return True
        
        # if i is in bound, but j is out of bound, return false.
        if j < 0:
            return False

        # if the current char is a star
        if j >= 0 and p[j] == '*':
            
            # check if there is a match of the current char in s and previous char in p(before *)
            match = (i >= 0) and (s[i] == p[j - 1] or p[j - 1] == '.')

            # if current charts match, then go dp(i-1, j), if no match, go check dp(i, j-2)
            return (match and self.dfs_prefix(s, p, i - 1, j)) or self.dfs_prefix(s, p, i, j - 2)
        
        #  if there is a match of the current char in s and p
        if i >= 0 and (s[i] == p[j] or p[j] == '.'):
            return self.dfs_prefix(s, p, i - 1, j - 1)
        
        return False

    # bottom up algorithm, start from dp(0,0) -> dp(n, n) 
    def dp_bottome_up_prefix(self, s, p):

        s_len, p_len = len(s), len(p)

        dp = [[False for col in range(p_len + 1)] for row in range(s_len + 1)]
        dp[0][0] = True
        
        # handle the pattern like a*, a*b* or a*b*c* for the 0th row
        for j in range(1, p_len + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]   

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    continue

                if p[j - 1] == '*':
                    
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                       dp[i][j] = dp[i - 1][j]
                    
                    dp[i][j] = (dp[i][j] or dp[i][j - 2])


        for i in dp:
            print(i)
            print()
            
        return dp[s_len][p_len]


s = 'aab'
p = 'c*a*b'

# s = 'aaa'
# p = 'aaaa'

# s = "a"
# p = ".*..a*"

s = 'aa'
p = 'a*'
sol = Solution()
print(sol.isMatch(s, p))

x = 'abc'
print(x[1:1])