import heapq as heap

'''
Q295: Find median from data stream

Solution 1: O(nlogn)
We only need a consistent way to access the median elements. Keeping the entire input sorted is not a requirement.
1. Use a max heap to store the smaller half of th data and a min heap to store the larger half of the data
2. Balance the heap sizes. Max-heap is allowed to store, at worst, one more element more than the min-heap. 
    Q: How to decide in which half we should put the new input
    2.1 if the max-heap is empty, then push the new input into it
    2.2 if the max-heap is not empty, then decide in which heap we should put the new element
        2.2.1 Two heap are the same size, then
            1. if the input is less than the smallest element of the larger half, then it belongs to the smaller half.
               push it directly into smaller half.
            2. if the input is larger than the top of larger half, then it belongs to the larger half. In order to maintain
               the balance property. Move the larger half's smallest element to the smaller half and then push the new 
               input to larger half.
        2.2.2 Max-heap is one more element more than the min-heap.
            1. if the input is larger than the top of smaller half(largest element), then it belong to the larger half.
               push it directly into larger half(min-hap)
            2. if the input is smaller than the top of smaller half, then it belongs to the smaller half. In order to
               maintain the balance property. Move the current largest element of smaller half to the larger half and then
               push the input into smaller half 

Leetcode version: O(nlogn)
1. The same as above
2. Balance the heap sizes. 
   2.1 Push the new input into smaller half.
   2.2 Move the largest element of smaller half to larger half
   2.3 Balance the heap size to maintain the heap property. That is Max-heap is larger than min-heap, move the top of 
       larger half to smaller half.
'''

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    # leetcode solution
    def add_num(self, num):

        # push new input into smaller half
        heap.heappush(self.max_heap, -num)

        # balance step, maintain the balance property
        # move the largest element of smaller half to larger half
        l_top = -heap.heappop(self.max_heap)
        heap.heappush(self.min_heap, l_top)

        # adjust size if necessary
        if len(self.max_heap) < len(self.min_heap):
            r_top = heap.heappop(self.min_heap)
            heap.heappush(self.max_heap, -r_top)

    # my own solution
    def add_num_1(self, num):

        min_size = len(self.min_heap)
        max_size = len(self.max_heap)

        if max_size == 0:
            heap.heappush(self.max_heap, -num)
        else:
            # 判断当前数是是属于左边还是右边
            if max_size == min_size:
                # 是否直接放入左半边取决于当前数是否小于右半边最小数
                if num <= self.min_heap[0]:
                    heap.heappush(self.max_heap, -num)
                else:
                    # 把右半边的最小数放入左半边
                    heap.heappush(self.max_heap, -self.min_heap[0])
                    # 弹出右半边最小数，并将新数压入右半边
                    heap.heappop(self.min_heap)
                    heap.heappush(self.min_heap, num)

            if max_size == (min_size + 1):
                # 是否直接放入右半边取决于当前数是否大于左半边最大数
                if num >= -self.max_heap[0]:
                    heap.heappush(self.min_heap, num)
                else:
                    # 弹出左半边最小数，并放入到右半边
                    heap.heappush(self.min_heap, -self.max_heap[0])
                    heap.heappop(self.max_heap)
                    # 将当前值压入左半边
                    heap.heappush(self.max_heap, -num)

    def find_median(self):

        min_size = len(self.max_heap)
        max_size = len(self.min_heap)
        if min_size == max_size:
            a = self.max_heap[0]
            b = self.min_heap[0]
            median = (b - a) / 2

        if min_size != max_size:
            median = -self.max_heap[0]

        return median

set()
# test case
obj = MedianFinder()
obj.add_num(1)
obj.add_num(0)
print(obj.find_median())

obj.add_num(3)
print(obj.find_median())

obj.add_num(5)
print(obj.find_median())

obj.add_num(2)
print(obj.find_median())

obj.add_num(0)
print(obj.find_median())

obj.add_num(1)
print(obj.find_median())