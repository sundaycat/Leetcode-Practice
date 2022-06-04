'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: s = "cbaebabacd", p = "abc" Output: [0,6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        char_freq = {}
        for i in range(len(p)):
            char = p[i]
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        
        start, end, match, rs = 0, 0, 0, []
        while end < len(s):
            char = s[end]
            if char in char_freq:
                char_freq[char] -= 1
                if char_freq[char] == 0:
                    match += 1

            if match == len(char_freq):
                rs.append(start)

            if len(p) == (end - start + 1):
                char = s[start]
                if char in char_freq:
                    if char_freq[char] == 0:
                        match -= 1
                    char_freq[char] += 1
                start += 1

            end += 1
            
        return rs