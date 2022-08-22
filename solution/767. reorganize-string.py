#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from heapq import *
'''
In each step, we  append one occurrence of the highest frequency character to the output string. We will not put this character back in the heap to ensure that no two same characters are adjacent to each other. In the next step, we should process the next most frequent character from the heap in the same way and then, at the end of this step, insert the character from the previous step back to the heap after decrementing its frequency.

1. find the frequence of each char in string
2. maintain a max heap of size of the string
3. iterate through the max heap, for each step
    3.1 pop out the heap top (freq, char) pair
    3.2 push the previous (freq, char) pair into current heap if there exists one
    3.3 save the current (freq, char) pair as previous pair.
'''
class Solution:

    # Solution 1
    def reorganizeString_1(self, s: str) -> str:

        # find the frequency of each char in str
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
        
        # build a maxheap with the dict above
        maxHeap = []
        for char, freq in dict.items():
            heappush(maxHeap, (-freq, char))
        
        prevFreq, prevChar = 0, None
        res = []
        while maxHeap:

            freq, char = heappop(maxHeap)

            # add the previous entry back in the heap if its frequency is greater than zero
            if prevChar and -prevFreq > 0:
                heappush(maxHeap, (prevFreq, prevChar))

            # append the current character to the result string and decrement its count
            res.append(char)
            prevFreq = freq + 1
            prevChar = char

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(res) if len(res) == len(s) else ""


    # Solution 2: reference: https://www.youtube.com/watch?v=2g_b1aYTHeg
    def reorganizeString_2(self, s: str) -> str:

        # find the frequency of each char in str
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
        
        # build a maxheap with the dict above
        maxHeap = []
        for char, freq in dict.items():
            heappush(maxHeap, (-freq, char))
        
        prev, res = None, ''
        while maxHeap:

            freq, char = heappop(maxHeap)
            freq += 1
            res += char

            # if previous exist, push it back to the maxheap. and set prev to Null
            if prev:
                heappush(maxHeap, prev)
                prev = None                
            
            # if freqency > 0, set prev to current item.
            if -freq > 0:
                prev = (freq, char)

        # if we were successful in appending all the characters to the result string, return it
        return res if len(res) == len(s) else ''

# @lc code=end

# a -> 3, b -> 1, c -> 1
print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaab"))
