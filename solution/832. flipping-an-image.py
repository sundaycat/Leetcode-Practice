#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
from typing import List

'''
1. Flip: We can flip the image in place by replacing ith element from left with the ith element from the right.

2. Invert: We can take XOR of each element with 1. If it is 1 then it will become 0 and if it is 0 then it will become 1
'''
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        C = len(image)
        for row in image:
            for i in range((C+1)//2):
                row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
        
        return image

# @lc code=end

image = [[1,1,0],[1,0,1],[0,0,0]]
rs = Solution().flipAndInvertImage(image)
