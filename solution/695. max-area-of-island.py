#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 0:
                    continue
                cur_area = self.helper(grid, r, c)
                max_area = max(max_area, cur_area)

        return max_area

    def helper(self, grid, row, col):

        # border check, to make sure we won't walk off the border
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0

        # base case, set the grid cell to 0
        if grid[row][col] == 0:
            return 0

        # set the grid cell to 0 before jumpping into next level to avoid infinity loop
        grid[row][col] = 0

        # recursive check through the four directions
        up = self.helper(grid, row - 1, col)
        rt = self.helper(grid, row, col + 1)
        dn = self.helper(grid, row + 1, col)
        lt = self.helper(grid, row, col - 1)

        # restore the grid cell statue
        # grid[row][col] = 1
        return (1 + up + rt + dn + lt)
        
        
# @lc code=end

grid = \
[
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]


s = Solution()
maxArea = s.maxAreaOfIsland(grid)
print(maxArea)

for r in range(len(grid)):
    print(grid[r])