def num_of_islands(grid):

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == '0':
                continue
            
            helper(grid, r, c)
            count += 1

    return count

def helper(grid, r, c):

    # border check, to make sure we won't walk off the border
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return

    # base case, set the grid cell to 0
    if grid[r][c] == '0':
        return

    # set the grid cell to 0
    grid[r][c] = '0'

    # recursive check through the four directions
    helper(grid, r - 1, c)
    helper(grid, r, c + 1)
    helper(grid, r + 1, c)
    helper(grid, r, c - 1)
    

'''
grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
       ]
'''

grid = [  
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
       ]
x = num_of_islands(grid)
print(x)