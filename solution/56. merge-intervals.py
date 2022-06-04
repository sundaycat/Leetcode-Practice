#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List

'''
1. Sort the intervals on the start time to ensure a.start <= b.start
2. If 'a' overlaps 'b' (i.e. b.start < a.end), we need to merge them into a new interval 'c' such that:
    c.start = a.start
    c.end = max(a.end, b.end
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals or len(intervals) == 0:
            return intervals        

        # sort the intervals on the start time. key parameter takes a function, and lamda returns a function object.
        intervals.sort(key=lambda x: x[0])
        
        start, end = intervals[0][0], intervals[0][1]
        rs = []
        for i in range(1, len(intervals)):
            
            # if there exists overlaps, adjust the 'end' 
            # 因为不确定后续是否还有重叠区间, 所以先不加入返回结果
            if intervals[i][0] <= end: 
                end = max(end, intervals[i][1])
            else:
                # non-overlaping intervals
                # 把当前区间放入返回结果, 并把start,end重置为下一区间
                rs.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        rs.append([start, end])
        return rs


intervals = [[1, 4], [5, 6]]
s = Solution()
print(s.merge(intervals))


# @lc code=end