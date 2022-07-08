'''
https://www.youtube.com/watch?v=Ph95IHmRp5M
https://www.youtube.com/watch?v=xFv_Hl4B83A

state space tree. Each queen represent one node, and it has n choice, where n is the number of the columns
'''
def solve_N_queens(n):

    res = []
    board = [['.' for i in range(n)] for j in range(n)]
    helper(res, 0, board, n)
    return res

def helper(res, row, board, size):
    '''
    DFS: put 'Q' row by row. For each row, we iterate through all columns to find a possible position for 'Q'
    '''
    if row == len(board[0]):
        res.append(construct(board))
        return
    
    for col in range(size):
        if validate(board, row, col, size):
            board[row][col] = 'Q'
            helper(res, row + 1, board, size)
            board[row][col] = '.'

def validate(board, row, col, size):
    '''
    Check the cells before the current rowl and see if there exists any conflicts
        no confict in rows: self explaintory as we put 'Q' row by row
        no confict in columns : c == col
        no confict in positive diagnoals: r + c = row + col
        no conflict in negative diagonals: r - c = row - col
    '''
    for r in range(row):
        for c in range(size):
            if board[r][c] == 'Q' and (c == col or r + c == row + col or r - c == row - col):
                return False
    return True

def construct(board):
    output = []
    for row in range(len(board)):
        output.append(''.join(board[row]))
    return output

x = solve_N_queens(5)
for row in x:
    print(row)
