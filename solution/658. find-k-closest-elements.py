#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start

'''
1. locate the right most element that is cloest to the target(array has duplicates)
2. check the neighbor of closest k-1 times to pick the k closest elements. Under the following condition, we move left:
    2.1. closest element is at the right most of the array
    2.2. left element is closer to target than the right element
    2.3  move right 

Time Complexity: O(logN + K)
'''
from heapq import *
from typing import List

class Solution:

    # Solution 1
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # find the position of the right most closest element
        lt, rt = 0, len(arr) - 1
        while lt < rt - 1:

            mid = (lt + rt) // 2
            if arr[mid] <= x:
                lt = mid
            else:
                rt = mid
        
        cloest = lt if abs(arr[lt] - x) <= abs(arr[rt] - x) else rt
        
        # iterate from center to determine which K element should include
        lt = rt = cloest
        while k > 1:

            # move left if rt reaches the end of array or left element is more closer than rt
            # right == len(arr) - 1 also guarantee that the right index won't be out of boundary
            if (rt == len(arr) - 1) or (lt > 0 and abs(arr[lt - 1] - x) <= abs(arr[rt + 1] - x)):
                lt -= 1
            else:
                rt += 1

            k -= 1

        return arr[lt : rt + 1]

    # Solution 2: use min heap to pick up the k elements.
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        lt, rt = 0, len(arr) - 1
        while lt < rt - 1:

            mid = (lt + rt) // 2
            if arr[mid] <= x:
                lt = mid
            else:
                rt = mid
        
        cloest = lt if abs(arr[lt] - x) <= abs(arr[rt] - x) else rt

        low, high = cloest - k + 1, cloest + k - 1

        low = max(0, low)
        high = min(high, len(arr) - 1)

        minHeap = []
        for i in range(low, high + 1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))
        
        rs = []
        for _ in range(k):
            diff, val = heappop(minHeap)
            rs.append(val)
            
        rs.sort()
        return rs

# @lc code=end

arr = [1,2,4,5,6]
k = 2
x = 3

arr = [1,1,1,10,10,10,11]
k = 2
x = 12

# ans = [1, 3]
arr = [0,0,0,1,3,5,6,7,8,8]
k = 2
x = 2

# ans = [1,2,3,4]
arr = [1,2,3,4,5]
k = 4
x = -1

rs = Solution().findClosestElements(arr, k, x)


print(rs)