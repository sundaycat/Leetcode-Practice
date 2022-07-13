#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# @lc code=start

from heapq import *

'''
Reference: check legacy code and notes of two heap.
'''
class MedianFinder:

    def __init__(self):
        
        self.minHeap = []
        self.maxHeap = []
        self.size = 0       
        
    def addNum(self, num: int) -> None:
        
        self.size += 1
        heappush(self.maxHeap, -num)

        # 如果min heap的top 大于 maxheap的最小元素, 则表示该top应该被还到minheap中.
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            maxTop = -heappop(self.maxHeap)
            heappush(self.minHeap, maxTop)
            
        # balacne the size of the two heaps
        # maxHeap元素比minHeap多2个及2个以上
        if len(self.maxHeap) - len(self.minHeap) >= 2:
            # move the top of max heap to min heap
            maxTop = -heappop(self.maxHeap)
            heappush(self.minHeap, maxTop)
        
        # maxHeap元素小于minHeap
        if len(self.maxHeap) < len(self.minHeap):
            minTop = heappop(self.minHeap)
            heappush(self.maxHeap, -minTop)


    def findMedian(self) -> float:

        #size = len(self.minHeap) + len(self.maxHeap)
        median = None
        if self.size % 2 == 0:
            median = (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            median = -self.maxHeap[0]
        
        return median
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
obj = MedianFinder()

obj.addNum(1)
obj.addNum(2)
obj.findMedian()
obj.addNum(3)
obj.findMedian()
