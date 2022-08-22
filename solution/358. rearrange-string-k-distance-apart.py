# aappa k = 3
from collections import deque
from heapq import *


def reorganize_string(s, k):

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
    
    queue, res = deque(), []
    while maxHeap:

        freq, char = heappop(maxHeap)

        # append the current char to the result string and decrement its count
        res.append(char)
        freq += 1

        # append to the queue
        queue.append((freq, char))

        # pop out the left most element from the queue every k elements(distinct)
        if len(queue) == k:
            freq, char = queue.popleft()
            if -freq > 0:
                heappush(maxHeap, (freq, char))
    
    # if we were successful in appending all the characters to the result string, return it
    return ''.join(res) if len(res) == len(s) else ''

# gmrPagimnor
print("Reorganized string: " + reorganize_string("Programming", 3))
print("Reorganized string: " + reorganize_string("mmpp", 2)) # mpmp
print("Reorganized string: " + reorganize_string("aab", 2))
print("Reorganized string: " + reorganize_string("aapa", 3)) # ''
print("Reorganized string: " + reorganize_string("aaapppccc", 3)) # ''

