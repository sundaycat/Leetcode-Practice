'''
Add variable to keep track of the minimum substring
s: string 
t: pattern
Input: s = "ADOBECODEBANC", t = "ABC"   Output: "BANC"
'''
import math

class Solution:

    def minWindow(self, s: str, pattern: str) -> str:
        
        char_freq = {}
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        
        start, end, match, min_len = 0, 0, 0, math.inf
        left, right = -1, -1
        while end < len(s):
            char = s[end]
            if s[end] in char_freq:
                char_freq[char] -= 1
                if char_freq[char] == 0:
                    match += 1
            
            # 如果pattern内所有的计数都为0, 则表示找到了一个符合条件的substring
            while match == len(char_freq):
                
                # keep track of the minimum substring
                if (end - start + 1) < min_len:
                    min_len = end - start + 1
                    left = start
                    right = end

                # shrink the window
                char = s[start]
                if char in char_freq:
                    if char_freq[char] == 0:
                        match -= 1
                    char_freq[char] += 1
                start += 1
            
            end += 1
        
        return '' if start == -1 and end == -1 else s[left : right + 1]

s = 'ADOBECODEBANC'
pattern = 'ABC'

s = "a"
pattern = "a"
x = Solution()
rs = x.minWindow(s, pattern)
print(rs)