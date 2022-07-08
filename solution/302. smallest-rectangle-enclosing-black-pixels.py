
from typing import List


class Solution:
    """
    1. recursively visit all the cells via DFS
    2. keep track of the border of the min area rectangle during DFS.
    """
    def min_area(self, image: List[List[str]], r: int, c: int) -> int:

        # min row index, max row index, min col index, max col index
        border = [r, r, c, c]
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]

        self.helper(image, visited, r, c, border)

        length = border[1] - border[0] + 1
        height = border[3] - border[2] + 1

        return length * height

                
    def helper(self, image, visited, r, c, border):

        # border check, to make sure we don't walk off the border and do not revisit a cell.
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or visited[r][c]:
            return 

        # base case, return if the cell is 0
        if image[r][c] == '0':
            return
        
        # keep track of the boundary of the minmum retangle,
        border[0], border[1] = min(r, border[0]), max(r, border[1])
        border[2], border[3] = min(c, border[2]), max(c, border[3])
        
        # set the cell to be a visited cell
        visited[r][c] = True

        # recursive iterate throuth the 4 directions
        self.helper(image, visited, r - 1, c, border)
        self.helper(image, visited, r, c + 1, border)
        self.helper(image, visited, r + 1, c, border)
        self.helper(image, visited, r, c - 1, border)

        # restore the cell to unvisited while return.
        visited[r][c] = False

image = ["1110","1100","0000","0000"]
x = 0
y = 1

image = ["0010","0110","0100"]
x = 0
y = 2
              
s = Solution()
area = s.min_area(image, x, y)
print(area)