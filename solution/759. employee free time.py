from heapq import *
from typing import List

'''
Note that each employee list is individually sorted. SweepLine Algorithm. Merge sort + min heap.
1. Build a min heap with the first interval's start time of each emplopyee
2. POP out the interval with smallest start time in heap and update the max ending accordingly
    2.1 if current interval's start time > previous interval's end time(max_end), then we observe non-overlapping
        2.1.1 save the no-overlapping gap to result. 
        2.1.2 update the max_end
        2.1.3 if there are more intervals for employee, add its next interval to the heap
    2.2 if previous and current interval overlap, then
        2.2.1 update the max_end
        2.2.2 if there are more intervals for employee, add its next interval to the heap
'''     
class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[int]:
        
        rs, min_heap = [], []

        # push the first interval of each employee into min heap
        for i in range(len(schedule)):
            # (interval.start, interval.end, empployee index, index in interval)
            heappush(min_heap, (schedule[i][0], schedule[i][1], i, 0))

        max_end = min_heap[0][1]
        while min_heap:
            
            # obtain the heap top interval's information
            (cur_start, cur_end, eIdx, idx) = heappop(min_heap)

            # if the current interval is not overlapping with the previous interval, then save it to rs
            if cur_start > max_end:
                rs.append([max_end, cur_start])
            
            # keep track of the max ending time for the intervals that pop out of the heap
            max_end = max(max_end, cur_end)
            
            # if there are more intervals available for the current employee, add their next interval
            if idx + 2 < len(schedule[eIdx]):
                idx += 2
                heappush(min_heap, (schedule[eIdx][idx], schedule[eIdx][idx+1], eIdx, idx))
            
        return rs


schedule = [[1,2,5,6],[1,3],[4,10]]
s = Solution()
rs = s.employee_free_time(schedule)
print(rs)
