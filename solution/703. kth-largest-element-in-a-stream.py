#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
from typing import List
from heapq import *

class KthLargest:
    '''
    1. iterate the array to add its elememnts into minheap, maintain the minheap of size K
    2. when adding a new number into min heap
        2.1 if the heap size is larger than K, then pop out the top element(smallest)
        2.2 if not, then return the heap top.
    '''
    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.minHeap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:

        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

kthLargest = KthLargest(3, [4, 5, 8, 2]);
print(kthLargest.add(3))  # return 4
print(kthLargest.add(5))  # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))  # return 8
print(kthLargest.add(4))  # return 8


kthLargest = KthLargest(1, []);
print(kthLargest.add(-3))   # return -3
print(kthLargest.add(-2))   # return -2
print(kthLargest.add(-4))   # return -2
print(kthLargest.add(0))   # return 0
print(kthLargest.add(4))    # return 4