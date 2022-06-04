'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example: s="oidbcaf", pattern="abc", Output: True

Time complexity: O(len(pattern) + len(s))
Space complexity: O(len(pattern))
'''
class Solution:

    def checkInclusion(self, pattern: str, s: str) -> bool:

        # record freq of every char in pattern
        char_freq = {}
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        
        start, end, match = 0, 0, 0
        while end < len(s):

            # decrement accordingly if char in 's' matches any char in 'pattern'.
            char = s[end]
            if char in char_freq:
                char_freq[char] -= 1
                if char_freq[char] == 0:
                    # the freq equals 0 implies a full match in patter
                    match += 1
            
            # return if a valid permutation found
            if len(char_freq) == match:
                return True
            
            # shrink window and restore the match indicator and freq map while chars sliding out the window
            if len(pattern) == (end - start + 1):
                char = s[start]
                if char in char_freq:
                    if char_freq[char] == 0:
                        match -= 1
                    char_freq[char] += 1
                start += 1
            
            end += 1
        
        return False




