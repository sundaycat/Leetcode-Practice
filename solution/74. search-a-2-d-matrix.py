#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        # tansform the 2D coordinator to 1D
        lt, rt = 0, rows * cols - 1
        while lt <= rt:
            
            # find the index of middle element
            mid = (lt + rt) // 2

            # calculate its corresponding row, col index
            row = mid // cols
            col = mid % cols
            
            if matrix[row][col] > target:
                rt = mid - 1
            
            if matrix[row][col] < target:
                lt = mid + 1

            if matrix[row][col] == target:
                return True
    
        return False
        
# @lc code=end

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

matrix = [[1],[3]]
target = 2

rs = Solution().searchMatrix(matrix, target)
print(rs)