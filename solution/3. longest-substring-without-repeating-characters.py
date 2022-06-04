# solution 1
class Solution:

    # solution 1
    def lengthOfLongestSubstring1(self, s: str) -> int:

        start, max_len, char_freq = 0, 0, {}
        for end in range(len(s)):
            
            char_rt = s[end]
            if char_rt not in char_freq:
                char_freq[char_rt] = 0
            char_freq[char_rt] += 1

            # if the dict length is longer than window lenght, then there exist overlap elements
            while len(char_freq) < (end - start + 1):

                char_lt = s[start]
                char_freq[char_lt] -= 1
                if char_freq[char_lt] == 0:
                    del char_freq[char_lt]

                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len

    # soltuion 2
    def lengthOfLongestSubstring2(self, s: str) -> int:
        
        start, max_len, char_freq = 0, 0, {}
        for end in range(len(s)):

            #Condition to move and shrink window: The next window starts from the index next to the last index of the repeating element. The start index only changes when the last repeated char fall inside the new slide window. Example abcbeaf
            if s[end] in char_freq and char_freq[s[end]] >= start:
                start = char_freq[s[end]] + 1
        
            char_freq[s[end]] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len

strs = 'ABCDBCBB'
strs = "cbbabcab"
s = Solution()
print(s.lengthOfLongestSubstring2(strs))
