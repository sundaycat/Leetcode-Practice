'''
'''
def solve_sudoku(board):

    # Find the position of the next empty cell
    row, col = find_next_pos(board)

    # which mean can't find any empty cells
    if row == -1 and col == -1:
        return True

    for i in range(1, 10):
        if is_valid(board, row, col, i):
            board[row][col] = str(i)
            if solve_sudoku(board):
                return True
            board[row][col] = '.'

    return False

def find_next_pos(board):

    for r in range(9):
        for c in range(9):
            if board[r][c] != '.':
                continue
            return r, c
            
    return -1, -1

def is_valid(board, row, col, i):

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


board = [
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

x = solve_sudoku(board)
for row in board:
    print(','.join(row))