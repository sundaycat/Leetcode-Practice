#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List

'''
Case Analysis:
1. if overlap occures:
    
    1.1. retain the interval with earilest end time and remove the other one, then move the indexes to next intervals. In detail
        A. if left interval end time < right interval end time, then keep the left interval as next left interval and move the right to the next interval
        B. if left interval end time >= right interval end time, then keep the right interval as next left interval and move current right to next interval
        C. if left interval end time == right interval end time, then keep either interval as next left interval and move the current right to the next interval. It can be combine with case B.
    1.2 count the removal intervals
    
2. if non-overlap occures:
        Move to next interval, that is, keep the current right interval as next left interval and move the current right to the next interval
'''

class Solution:

    # orignal solution
    def eraseOverlapIntervals_1(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        left, right, count = 0, 1, 0
        while right < len(intervals):

            overlap_st = max(intervals[left][0], intervals[right][0])
            overlap_ed = min(intervals[left][1], intervals[right][1])

            if overlap_st < overlap_ed:

                count += 1
                if intervals[left][1] < intervals[right][1]:
                    right += 1  
                elif intervals[left][1] > intervals[right][1]:
                    left = right
                    right += 1
                else: #intervals[left][1] == intervals[right][1]:
                    left = right
                    right += 1
            else:
                left = right
                right += 1
        
        return count

    # optimize the code
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        left, right, count = 0, 1, 0
        while right < len(intervals):

            overlap_st = max(intervals[left][0], intervals[right][0])
            overlap_ed = min(intervals[left][1], intervals[right][1])
            
            # non-overlapping
            if overlap_st >= overlap_ed:
                left = right
                right += 1
                continue
            
            # overlapping
            count += 1
            if intervals[left][1] >= intervals[right][1]:
                left = right
            right += 1

        return count
        

# @lc code=end

# 2
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,100],[11,22],[1,11],[2,12]]
intervals = [[1,2],[1,3],[1,4]]

s = Solution()
rs = s.eraseOverlapIntervals(intervals)
print(rs)



