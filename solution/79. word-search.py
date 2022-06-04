def word_search(board, word):

    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != word[0]:
                continue
            
            if helper(board, word, r, c, 0, visited):
                return True
    
    return False


def helper(board, word, row, col, index, visited):

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col]:
        return False

    if board[row][col] != word[index]:
        return False

    if index == len(word) - 1:
        return True
    
    visited[row][col] = True
    up = helper(board, word, row - 1, col, index + 1, visited)
    rt = helper(board, word, row, col + 1, index + 1, visited)
    dn = helper(board, word, row + 1, col, index + 1, visited)
    lt = helper(board, word, row, col - 1, index + 1, visited)
    visited[row][col] = False
    
    return up or rt or dn or lt



# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(word_search(board, word))