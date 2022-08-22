#
# @lc app=leetcode id=1000 lang=python3
#
# [1000] Minimum Cost to Merge Stones
#

# @lc code=start
from heapq import heappop, heappush
from typing import List



class Solution:

    # each move consists of merging exactly k consecutive piles.
    def mergeStones(self, stones: List[int], k: int) -> int:
    
# @lc code=end

