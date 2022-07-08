#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if not self.isValid(row, col, board):
                    return False

        return True

    def isValid(self, row, col, board):
        
        # are there conflicts on the rows or cols
        for i in range(9):
        
            if (i != row and board[i][col] == board[row][col]) or \
                (i != col and board[row][i] == board[row][col]):
                return False
      
        # are they conflicts on the square
        rSt, rEd = (row // 3) * 3, (row // 3) * 3 + 3
        cSt, cEd = (col // 3) * 3, (col // 3) * 3 + 3
        for r in range(rSt, rEd):
            for c in range(cSt, cEd):
                if (r != row and c != col) and board[r][c] == board[row][col]:
                    return False
        
        return True

# @lc code=end

board = \
[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
print(s.isValidSudoku(board))
