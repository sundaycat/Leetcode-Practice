"""
Solution 1: Expand around center
Observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center.
"""
def longestPalindrome(s):

    if not s or len(s) == 0:
        return s

    # Go through all possible center position, expand from each center and check if there exist an palindrome. 
    start, end = 0, 0
    for i in range(len(s)):
        # handle cases that the length of s is odd, like "aba"
        start, end = is_palindrome(s, i, i, start, end)
        # handle case that the length of s is even, like "bb" or "abba"
        start, end = is_palindrome(s, i, i+1, start, end)
    
    return s[start:end+1]
    
def is_palindrome(s, low, high, start, end):
    
    while low >= 0 and high < len(s):

        if s[low] != s[high]:
            break
        
        low -= 1
        high += 1
    
    if high - low - 1 > (end - start + 1):
        start = low + 1
        end = high - 1
    
    return start, end

s = "babad"
print(longestPalindrome(s))

# solution 2: dynamic programming
# 相比暴力解， 动态循环使用数组记录(i,j)的回文，在判断新字段是否为回文时，只需要调用先前的判断结果，而不需要重新判断，从而节约了时间。

# abcba
'''
(1) s[start] == s[end]
(2) non-boundary substring should be palindrome

states table:
  0 1 2 3 4
0 1 0     1
1   1 0 1
2     1 0
3       1 0
4         1
'''
def longest_palindrome_2(s):

    pali_stat = [[False for x in range(0, len(s))] for x in range(0, len(s))]
    max_len = 0
    start, end = 0, 0
    # starting from str length = 0, 1, 2, 3, ...
    for j in range(0, len(s)):
        for i in range(0, j):
            # 便利标注[i,j]之间的所有回文, (i+1, j-1)表示(i,j)中间的字符串.
            if s[i] == s[j] and (j - i <= 2 or pali_stat[i + 1][j - 1] == True):

                pali_stat[i][j] = True
                if max_len < j - i + 1:
                    max_len = j - i + 1
                    start = i
                    end = j

                # 如果找到第一个回文之后便跳出循环会导致该次循环中的某些内置回文没有被标注，而这会影响到后续的回文判断
                # break

    return s[start:end + 1]


test = "abaxabaxabb"
print(longest_palindrome_1(test))
print(longest_palindrome_2(test))
