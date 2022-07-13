#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
import math
from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        maxPath = -math.inf
        visited = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                path = self.helper(row, col, matrix, -math.inf, visited)                
                maxPath = max(maxPath, path)
        
        return maxPath

    def helper(self, row, col, matrix, prev, visited):

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return 0

        if matrix[row][col] <= prev:
            return 0

        if visited[row][col]:
            return visited[row][col]

        up = self.helper(row - 1, col, matrix, matrix[row][col], visited)
        rt = self.helper(row, col + 1, matrix, matrix[row][col], visited)
        dn = self.helper(row + 1, col, matrix, matrix[row][col], visited)
        lt = self.helper(row, col - 1, matrix, matrix[row][col], visited)

        visited[row][col] = max(up, rt, dn, lt) + 1
        return visited[row][col]

# @lc code=end

# matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [
    [0,1,2,3,4,5,6,7,8,9],
    [19,18,17,16,15,14,13,12,11,10],
    [20,21,22,23,24,25,26,27,28,29],
    [39,38,37,36,35,34,33,32,31,30],
    [40,41,42,43,44,45,46,47,48,49],
    [59,58,57,56,55,54,53,52,51,50],
    [60,61,62,63,64,65,66,67,68,69],
    [79,78,77,76,75,74,73,72,71,70],
    [80,81,82,83,84,85,86,87,88,89],
    [99,98,97,96,95,94,93,92,91,90],
    [100,101,102,103,104,105,106,107,108,109],
    [119,118,117,116,115,114,113,112,111,110],
    [120,121,122,123,124,125,126,127,128,129],
    [139,138,137,136,135,134,133,132,131,130],
    [0,0,0,0,0,0,0,0,0,0]
]
# matrix = [[9,9,4],[6,6,8],[2,1,1]]


s = Solution()
rs = s.longestIncreasingPath(matrix)
print(rs)