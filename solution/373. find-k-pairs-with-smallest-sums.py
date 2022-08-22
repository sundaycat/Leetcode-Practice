#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
from typing import List
from heapq import *

class Solution:
    '''
    Solution: 
    
    1. we go through all the numbers of the two input arrays to create piars and initally insert them all in the heap until we have k pairs in a Max heap.
    2. when there are K pairs in max heap

        2.1 if a new pair is larger than the top pair in the max heap, we can 'break' the loop. Since the arrays are sorted in the ascending order, we'll not be able to find a pair with a smaller sum moving forward.
        2.2 if a new pair is smaller than the top pair in the max heap, we remove the largest pair and insert the new piar into the heap.

    Time complexity: o(NMlogK), where N and M are the total number of elements in both arrays.
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        maxHeap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                
                if len(maxHeap) < k: 
                    # insert the numbers into the heap when the elements in heap are less than K 
                    item = (-(nums1[i] + nums2[j]), i, j)  
                    heappush(maxHeap, item)
                else:
                    # if the pair sum is larger than heap top, then we 'break' because we can't find a pair sum smaller moving foward.
                    if nums1[i] + nums2[j] > -maxHeap[0][0]:
                        break
                    else:
                        # we have a pair with smaller sum, remove top and insert this pair in heap
                        heappop(maxHeap)
                        item = (-(nums1[i] + nums2[j]), i, j)
                        heappush(maxHeap, item)
        
        res = []
        for num, i, j in maxHeap:
            res.append([nums1[i], nums2[j]])

        return res
        
# @lc code=end


