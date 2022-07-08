#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:

    '''
    Solution 1: 记录下当前cell的值, 并替换为一个特殊字符, 来避免重复访问
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] != word[0]:
                    continue

                if self.helper(board, word, 0, r, c):
                    return True
        
        return False
    
    
    def helper(self, board, word, index, r, c):

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False

        if board[r][c] != word[index]:
            return False
        
        if index == len(word) - 1:
            print('r: {} c: {}'.format(r, c))
            print(index)
            return True
        
        # turn the visited cell to '#' to avoid revisiting, ABCB
        temp = board[r][c]
        board[r][c] = '#'

        # recursivly expore the 4 directions
        up = self.helper(board, word, index + 1, r - 1, c)
        rt = self.helper(board, word, index + 1, r, c + 1)
        dn = self.helper(board, word, index + 1, r + 1, c)
        lt = self.helper(board, word, index + 1, r, c - 1)

        # restore the cell to its original value.
        board[r][c] = temp

        return (up or rt or dn or lt)

    '''
    Solution 2: 用布尔array来避免重复访问
    '''
    def word_search(self, board, word):

        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != word[0]:
                    continue
                
                if self.helper_2(board, word, r, c, 0, visited):
                    return True
        
        return False


    def helper_2(self, board, word, row, col, index, visited):

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col]:
            return False

        if board[row][col] != word[index]:
            return False

        if index == len(word) - 1:
            return True
        
        visited[row][col] = True
        up = self.helper(board, word, row - 1, col, index + 1, visited)
        rt = self.helper(board, word, row, col + 1, index + 1, visited)
        dn = self.helper(board, word, row + 1, col, index + 1, visited)
        lt = self.helper(board, word, row, col - 1, index + 1, visited)
        visited[row][col] = False
        
        return up or rt or dn or lt

# @lc code=end

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

# 如果不标记已经访问过的cell, "ABC" C向左重复访问B, 会得到true的结果.
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

s = Solution()
print(s.exist(board, word))