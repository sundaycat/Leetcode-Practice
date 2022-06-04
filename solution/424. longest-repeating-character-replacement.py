class Solution:

    '''
    1. char_freq count and updates the char frequent of current window and updates accordingly as the window moves forward. so it dosen't need to delete the elements when the count become 0.
    2. window length - window max_count > windown length - global max_count > k. If window length - most_count > k are true, it guarnteed that window length - windonw max_count must be ture. Thus, the window should shrink accordingly.
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        
        start, end, max_len, max_count = 0, 0, 0, 0

        char_freq = {}
        while end < len(s):

            if s[end] not in char_freq:
                char_freq[s[end]] = 0
            char_freq[s[end]] += 1
        
            max_count = max(max_count, char_freq[s[end]])
            if end - start + 1 - max_count > k:
                char_freq[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
            end += 1
        
        return max_len

