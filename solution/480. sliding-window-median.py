#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
from typing import List
from heapq import *

'''
1. insert a new number into the corresponding heap and rebalance the size of heap
2. when current window size == k:
    - calculate and record the median of current window.
    - remove the number from the heaps which is going out of the sliding window
        - searching the element in the heap, size of k.   O(k)
        - swap the last element of heap to the pos of element being remove.  O(1)
        - adjust the heap upper and down from that position. O(logK)
    - reblance the size of heap if necessary(only max_heap needs). O(logK)
'''
class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        minHeap, maxHeap = [], []

        start, rs = 0, []
        for end in range(len(nums)):

            # insert new elements into the heap and rebalance the heap
            heappush(maxHeap, -nums[end])
            if minHeap and -maxHeap[0] > minHeap[0]:
                heappush(minHeap, -heappop(maxHeap))
            
            # rebalance the heap size if necessary
            self.rebalance(minHeap, maxHeap)

            # onnce the size of windown equals K 
            if end - start + 1 == k:

                # calculate median and save the result
                median = 0
                if (len(minHeap) + len(maxHeap)) % 2 == 0:
                    median = (minHeap[0] - maxHeap[0]) / 2
                else:
                    median = -maxHeap[0]
                rs.append(median)

                # remove element from the window and move forward
                toBeRemove = nums[start]
                if toBeRemove <= -maxHeap[0]:
                    self.remove(maxHeap, -toBeRemove)
                else:
                    self.remove(minHeap, toBeRemove)
                
                # rebalance the heap size if necessary
                self.rebalance(minHeap, maxHeap)

                start += 1
        
        return rs

    
    def rebalance(self, minHeap, maxHeap):

        # the size of smaller half is less than larger half
        # maxHeap: 1, minHeap: 2,3
        if len(maxHeap) < len(minHeap):
            heappush(maxHeap, -heappop(minHeap))

        # the size of smaller half exceed larger half more than 1 element
        # maxHeap:1, 2, 3, minHeap: 5
        if len(maxHeap) >= len(minHeap) + 2:
            heappush(minHeap, -heappop(maxHeap))


    def findIndex(self, array, target):

        for i in range(len(array)):
            if array[i] == target:
                return i
        
        return -1
    
    def remove(self, heap, target):

        # find the index of the target element in heap
        index = self.findIndex(heap, target)

        # swap it with the last element in heap and remove it.
        heap[index] = heap[-1]
        del heap[-1]

        # swap upper and downward from current index to maintain heap property.
        if index < len(heap):
            self.shiftDown(heap, index)
            self.shiftUp(heap, index)

    def shiftUp(self, heap, curIdx):
        
        while curIdx >= 0:
            # (i - 1) / 2
            parent = (curIdx - 1) >> 1
            if parent >= 0 and heap[curIdx] < heap[parent]:
                heap[curIdx], heap[parent] = heap[parent], heap[curIdx]
            curIdx = parent
    
    def shiftDown(self, heap, curIdx):

        smaller = curIdx
        while curIdx < len(heap):

            # i * 2 + 1, i * 2 + 2
            left = (curIdx << 1) + 1
            right = (curIdx << 1) + 2

            if left < len(heap) and heap[left] < heap[smaller]:
                smaller = left
            if right < len(heap) and heap[right] < heap[smaller]:
                smaller = right

            if smaller == curIdx:
                break
            
            heap[curIdx], heap[smaller] = heap[smaller], heap[curIdx]
            curIdx = smaller



        
# @lc code=end

nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
rs = s.medianSlidingWindow(nums, k)
print(rs)

