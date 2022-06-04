def max_area_of_island(grid):

    max_area = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == 0:
                continue
            cur_area = helper(grid, r, c)
            max_area = max(max_area, cur_area)

    return max_area

def helper(grid, row, col):

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0

    if grid[row][col] == 0:
        return 0

    grid[row][col] = 0

    up = helper(grid, row - 1, col)
    rt = helper(grid, row, col + 1)
    dn = helper(grid, row + 1, col)
    lt = helper(grid, row, col - 1)

    return (1 + up + rt + dn + lt)


grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]

x = max_area_of_island(grid)
print(x)