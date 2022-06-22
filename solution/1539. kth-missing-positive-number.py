#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
from array import array
from typing import List

class Solution:

    '''
    O(N+K) cylic sort
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:

        i, extra = 0, set()
        while i < len(arr):
            j = arr[i] - 1
            if arr[i] <= len(arr) and i != j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[i] > len(arr):
                    extra.add(arr[i])
                i += 1

        for i in range(len(arr) + k):

            if (i < len(arr) and i != arr[i] - 1) \
                or (i >= len(arr) and i + 1 not in extra):

                k -= 1
            
            if k == 0: return i + 1

    '''
    O(logN) binary search
    '''
        
# @lc code=end

