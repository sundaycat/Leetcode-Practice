from heapq import *

def findMaxNumOfUniqueInts(nums, k):

    # find the frequency of each number
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1
    
    # insert all numbners into a minheap
    minHeap = []
    for num, freq in dict.items():
        heappush(minHeap, (freq, num))
    
    # follwoing a greedy approach, trying removing the least frequent number first from the min heap, 
    count = 0
    while minHeap and k > 0:
        
        freq, num = heappop(minHeap)

        # to make an element distinct, we need to remove all of its occurrences except one. if freq == 1, then k won't change.
        k -= freq - 1
        if k >= 0:
            count += 1

    # if k > 0, means we have to remove some distinct numbers.
    if k > 0:
        count -= k

    return count

nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
k = 2

nums = [3, 5, 12, 11, 12]
k = 3

rs = findMaxNumOfUniqueInts(nums, k)
print(rs)