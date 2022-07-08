#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(0, 0, board)


    def helper(self, row, col, board):

        for r in range(row, 9):
            for c in range(9):
                
                if (r == row and c < col) or board[r][c] != '.':
                    
                    # return if we hits the last cell
                    if r == 8 and c == 8:
                        return True
                    continue                    
                
                for i in range(1, 10):
                    if self.isValid(board, r, c, i):
                        board[r][c] = str(i)
                        if self.helper(r, c, board):
                            return True
                        board[r][c] = '.'
                
                return False
    
    
    def isValid(self, board, row, col, i):

        for r in range(9):
            if board[r][col] == '.':
                continue
            if r != row and board[r][col] == str(i):
                return False

        for c in range(9):
            if board[row][c] == '.':
                continue
            if c != col and board[row][c] == str(i):
                return False

        r_st, r_ed = (row // 3) * 3, (row // 3) * 3 + 3
        c_st, c_ed = (col // 3) * 3, (col // 3) * 3 + 3
        for r in range(r_st, r_ed):
            for c in range(c_st, c_ed):
                if board[r][c] == '.':
                    continue

                if board[r][c] == str(i):
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
s.solveSudoku(board)
for row in board:
    print(','.join(row))