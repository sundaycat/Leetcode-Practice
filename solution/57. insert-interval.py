#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:

    '''
    Solution 1: time complexity: O(NlogN), space complexity: O(N)
    '''
    def insert_1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # insert into the intervals and sort it by start
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        # iterate through array and merge the intervals
        rs = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):

            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                # save the current interval and move to the next non-overlaping interval
                rs.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        rs.append([start, end])
        return rs 
    
    '''
    Solution 2: because the interval has been sorted already, instead of append and sorting the intervals, we can find the position to insert the bowl. This can reduce the time complexity to O(N)
    '''
    def insert_opt(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        rs = []

        # skip all intervals that come before the "new interval"
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            rs.append(intervals[i])
            i += 1
        
        # merge all intervals that overlap with the "new interval"
        # 第一个while loop 保证了 new.st < cur.ed, 要想不重合, 还需要保证 new.ed >= cur.st, 同时由于合并后的新区间与后续的interval都自动满足 new.st < cur.ed, 我们只需要保证 new.ed >= cur.st就能判断他们是否重合.
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        rs.append(newInterval)

        # add all the remaining intervals to the output
        while i < len(intervals):
            rs.append(intervals[i])
            i += 1

        return rs

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = []
newInterval = [4, 8]

intervals = [[1, 5]]
newInterval = [0, 0]

intervals = [[1,5]]
newInterval = [6,8]

s = Solution()
rs = s.insert(intervals, newInterval)
print(rs)


# @lc code=end

