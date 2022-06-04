'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Time complexity:    O(N + N) = O(N)
Space complexity:   O(K)
'''
import math

def longest_substring_with_k_distinct(str, k):

    char_freq = {}

    start, end, max_len = 0, 0, -math.inf
    for end in range(len(str)):

        rt_char = str[end]
        if rt_char not in char_freq:
            char_freq[rt_char] = 0
        char_freq[rt_char] += 1

        # shrink the window until the number of distinct characters <= k
        # 大于K时才收缩窗口, 否则max_len捕捉不到等于K时的长度.
        while len(char_freq) > k:

            lt_char = str[start]

            char_freq[lt_char] -= 1
            if char_freq[lt_char] == 0:
                del char_freq[lt_char]

            start += 1

    max_len = max(end - start + 1, max_len)

    return max_len


print(longest_substring_with_k_distinct("cbbebi", 10))
