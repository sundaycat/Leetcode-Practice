#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from heapq import heappop, heappush


class Solution:

    '''
    Solution:
    
        1. count occurence of each letter O(N)
        2. maintain a maxheap of size k, where k is the distinct character O(klogk)
        3. reconstruct the string by max heap O(N)

    Complexity: O(N + klogk), in the worst case when all characters are distinct, O(NlogN)
    '''
    def frequencySort(self, s: str) -> str:
        
        # count the occurence of each letter
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        # maintain a maxheap of size k, where k is the distinct character
        maxHeap = []
        for char, frequency in freq.items():
            heappush(maxHeap, (-frequency, char))

        # reconstruct the string by max heap O(N)
        rs = []
        while maxHeap:
            freqency, char = heappop(maxHeap)
            for _ in range(-freqency):
                rs.append(char)
        
        return ''.join(rs)
                

# @lc code=end

s = 'tree'
s = 'cccaaa'
s = 'Aabb'
rs = Solution().frequencySort(s) 
print(rs)