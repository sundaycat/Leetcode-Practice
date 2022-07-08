"""
This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”.
Reference: https://www.geeksforgeeks.org/find-number-of-islands/
"""

class Graph(object):
    '''
    SOLUTION 1
    '''
    def __init__(self, row, col, graph):

            self.row = row
            self.col = col
            self.graph = graph

    # A utility function to do DFS for a 2D boolean matrix. It only considers the 4 neighbours as adjacent vertices
    def DFS(self, row, col, visited):

        # These arrays are used to get row and column numbers of 4 neighbours of a given cell
        rowIdx = [0, -1, 0, 1]
        colIdx = [-1, 0, 1, 0]

        # Mark current cell as visited
        visited[row][col] = True

        # Recur for all connected neighbours
        for nbr in range(4):

            rowOfNbr, colOfNbr = row + rowIdx[nbr], col + colIdx[nbr]
            isSafe = 0 <= rowOfNbr < self.row and 0 <= colOfNbr < self.col and \
                     not visited[rowOfNbr][colOfNbr] and self.graph[rowOfNbr][colOfNbr]

            if isSafe:
                self.DFS(rowOfNbr, colOfNbr, visited)

    # The main function that returns count of islands in a given boolean 2D matrix
    def countIslands(self):

        # Make a bool array to mark visited cells. Initially all cells are unvisited
        visited = [[False for i in range(self.col)] for j in range(self.row)]

        # Initialize number of islands as 0 and traverse through the all cells of given matrix
        numOfIslands = 0
        for row in range(self.row):
            for col in range(self.col):
                # If a cell with value 1 is not visited yet, then new island found
                if not visited[row][col] and self.graph[row][col] == 1:
                    # Visit all cells in this island and increment island count
                    self.DFS(row, col, visited)
                    numOfIslands += 1

        return numOfIslands


    '''
    SOLUTION 2
    '''
    def num_of_islands(self, grid):

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == '0':
                    continue
                
                self.helper(grid, r, c)
                count += 1

        return count


    def helper(self, grid, r, c):

        # border check, to make sure we won't walk off the border
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return

        # base case, if the grid cell is 0, return
        if grid[r][c] == '0':
            return

        # set the grid cell to 0
        grid[r][c] = '0'

        # recursive check through the four directions
        self.helper(grid, r - 1, c)
        self.helper(grid, r, c + 1)
        self.helper(grid, r + 1, c)
        self.helper(grid, r, c - 1)


graph = \
[
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)
print(g.countIslands())


grid = \
[
    ['1', '1', '0', '0', '0'],
    ['0', '1', '0', '0', '1'],
    ['1', '0', '0', '1', '1'],
    ['0', '0', '0', '0', '0'],
    ['1', '0', '1', '0', '1']
]
print(g.num_of_islands(grid))