'''
可能会先碰到不在边界上的点, 但最后连接到边界. 所以只能先把边界上的点及其相联的点都换成0.
最后再遍历一遍矩阵,得出飞地面积.
'''
def num_of_enclaves(grid):

    r_boundary = [0, len(grid) - 1]
    c_boundary = [0, len(grid[0]) - 1]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            
            # skip counting if the cell is water or not on the boundary
            if grid[r][c] == 0 or (r not in r_boundary and c not in c_boundary):
                continue
            
            # changes all 1s to 0 if the land is connected to the boundary
            helper(grid, r, c)
    
    count = 0    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                continue
            count += 1
    
    return count

def helper(grid, r, c):

    # border check, to make sure we won't walk off the border
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return

    # base case, stop if we encounter symbol 'X' or '#'
    if grid[r][c] == 0:
        return

    # set the grid cell to 0
    grid[r][c] = 0

    # recursive check through the four directions
    helper(grid, r - 1, c)
    helper(grid, r, c + 1)
    helper(grid, r + 1, c)
    helper(grid, r, c - 1)


grid = [
            [0,0,0,1,1,1,0,1,0,0],
            [1,1,0,0,0,1,0,1,1,1],
            [0,0,0,1,1,1,0,1,0,0],
            [0,1,1,0,0,0,1,0,1,0],
            [0,1,1,1,1,1,0,0,1,0],
            [0,0,1,0,1,1,1,1,0,1],
            [0,1,1,0,0,0,1,1,1,1],
            [0,0,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,0,0,0,0],
            [0,0,0,0,1,1,0,0,0,1]
        ]
x = num_of_enclaves(grid)
print(x)
for i in grid:
    print(i)