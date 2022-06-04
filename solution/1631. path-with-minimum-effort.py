from typing import List
import heapq

class Solution:

    '''
    1. consider the grid as aa graph where adjacent cells have an edge with cost  of the difference between the cells
    2. if you ar given threshold k, check it is possible to go from (0, 0 ) to (n-1, m-1) using only edges of <= k cost
    3. binary search the k value
    '''
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows, cols = len(heights), len(heights[0])
        
        # effort, row, col
        min_heap = [(0, 0, 0)]
        visited = set()
        while min_heap:

            rc_effort, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == rows - 1 and c == cols - 1:
                return rc_effort

            # relax the edges going out of node <r, c>, d(<x, y>) = max(d(<r,c>), w(<r,c> -> <x,y>))
            height = heights[r][c]
            if r - 1 >= 0:
                upper = abs(heights[r - 1][c] - height)
                upper_effort = max(rc_effort, upper)
                heapq.heappush(min_heap, (upper_effort, r - 1, c))
            if c + 1 < cols:
                right = abs(heights[r][c + 1] - height)
                right_effort = max(rc_effort, right)
                heapq.heappush(min_heap, (right_effort, r, c + 1))
            if r + 1 < rows:
                down = abs(heights[r + 1][c] - height)
                down_effort = max(rc_effort, down)
                heapq.heappush(min_heap, (down_effort, r + 1, c))
            if c - 1 >= 0:
                left = abs(heights[r][c - 1] - height)
                left_effort = max(rc_effort, left)
                heapq.heappush(min_heap, (left_effort, r, c - 1))


# heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
# heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
s = Solution()
x = s.minimumEffortPath(heights)
print(x)