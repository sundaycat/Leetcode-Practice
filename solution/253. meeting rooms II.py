from heapq import *
import math
from typing import List
 

class Solution:

    def minMeetingRooms(self, meetings: List[List[int]]) -> int:

        start, end = 0, 1
        meetings.sort(key=lambda x: x[start])

        min_rooms, min_heap = -math.inf, []
        for incoming in meetings:
            # remove all the active meetings that end before the incoming meeting
            while len(min_heap) > 0 and incoming[start] >= min_heap[0][end]:
                heappop(min_heap)
            
            # push the incoming meeting into the heap
            heappush(min_heap, incoming)

            # keep track of the minimum rooms require for all meeting
            min_rooms = max(min_rooms, len(min_heap))
        
        return min_rooms


meetings = [[4,5], [2,3], [2,4], [3,5]]
s = Solution()
print(s.minMeetingRooms(meetings))