#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from typing import List


class Solution:

    '''
    1. Turn the 'O's that connect to border to a special symbol '#' via DFS
    2. iterate through board and flip the remaing 'O' to 'X'
    3. restore the '#' to 'O'
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 1. Turn the 'O's that connect to border to a special symbol '#'
        rBorder = [0, len(board) - 1]
        cBorder = [0, len(board[0]) - 1]
        for r in range(len(board)):
            for c in range(len(board[0])):
    
                if board[r][c] == 'X':
                    continue
                
                if r in rBorder or c in cBorder:
                    self.helper(board, r, c)

        # 2. iterate through board and flip the remaing 'O' to 'X'
        # 3. restore the '#' to 'O'
        for r in range(len(board)):
            for c in range(len(board[0])):    
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
                if board[r][c] == '#':
                    board[r][c] = 'O'


    def helper(self, board, r, c):

        # border check, to make sure we won't walk off the border
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        
        # base case, stop if we encounter symbol 'X' or '#', avoidng infinity loop
        if board[r][c] == 'X' or board[r][c] == '#':
            return
        
        board[r][c] = '#'
        
        # recursive check through the four directions
        self.helper(board, r - 1, c)
        self.helper(board, r, c + 1)
        self.helper(board, r + 1, c)
        self.helper(board, r, c - 1)

            
# @lc code=end

board = \
[
    ["X","X","X","X","X"],
    ["X","X","O","O","X"],
    ["X","O","X","O","X"],
    ["X","O","O","X","X"]
]

s = Solution()
s.solve(board)
for r in range(len(board)):
    print(board[r])