
def surrounded_regions(grid):

    # Turn the 'O's that connect to border to a special symbol '#'
    r_border = [0, len(grid) - 1]
    c_border = [0, len(grid[0]) - 1]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'X':
                continue
            
            if r in r_border or c in c_border:
                helper(grid, r, c)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                grid[r][c] = 'X'
            
            if grid[r][c] == 'I':
                grid[r][c] = 'O'

def helper(grid, r, c):

    # border check, to make sure we won't walk off the border
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return

    # base case, stop if we encounter symbol 'X' or '#'
    if grid[r][c] == 'X' or grid[r][c] == '#':
        return
    
    grid[r][c] = '#'

    # recursive check through the four directions
    helper(grid, r - 1, c)
    helper(grid, r, c + 1)
    helper(grid, r + 1, c)
    helper(grid, r, c - 1)
 


grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
for i in grid:
    print(i)
print()
surrounded_regions(grid)
for i in grid:
    print(i)