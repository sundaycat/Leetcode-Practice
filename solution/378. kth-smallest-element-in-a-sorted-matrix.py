#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
from typing import List
from heapq import *


class Solution:
    
    '''
    Solution: using heap

        1. push the first element of each row into a min heap
        2. pop out the smallest element(top) from current heap
        3. push the next element of the same row into the min heap.
        4. continue 2, 3 until we reach kth element

    Time complexity: O(Klog(row)), where row is len(matrix)
    Space Complexity: O(row)
    '''
    def kthSmallest_1(self, matrix: List[List[int]], k: int) -> int:
        
        # add the first element into the heap
        minHeap = []
        for row in range(len(matrix)):
            item = (matrix[row][0], row, 0)
            heappush(minHeap, item)

        count = 0
        while minHeap:       
            
            (val, row, col) = heappop(minHeap)

            count += 1
            if count == k: return val

            if col + 1 < len(matrix[0]):
                item = (matrix[row][col + 1], row, col + 1)
                heappush(minHeap, item)
        
        return -1

    '''
    Solution: Binary Search. 

    1. Applying the binary search on the "number range" instead of the "index range". 
    2. count the elements that is less or equal to middle.

    even if there are k elemnts in the array that is less than the current mid, it may not be the desired answer and there stil could be some elements on the left of mid that meets the requirment(> k elements). so the answer we are looking for should the smallest element(right most) that has k elements less or equal to it.

    reference:  https://www.youtube.com/watch?v=0jRTsLB8W_M
                https://www.youtube.com/watch?v=oeQlc87HbbQ
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        lt, rt = matrix[0][0], matrix[n-1][n-1]

        kth = 0
        while lt <= rt:

            mid = (lt + rt) // 2
            count = self.countLessEqualToMid(matrix, mid)
            if count >= k:
                kth = mid
                rt = mid - 1
            else:
                lt = mid + 1

        return kth
    '''
    smaller: the largest number that is <= middle number
    larger: the smallest number that is > middle number
    '''
    def countLessEqualToMid(self, matrix, mid):

        row, col = len(matrix) - 1, 0
    
        count = 0
        while row >= 0 and col < len(matrix):
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1             

        return count


# @lc code=end

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

# matrix = [[-5]]
# k = 1
print(Solution().kthSmallest(matrix, k))