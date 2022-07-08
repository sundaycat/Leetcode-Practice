#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
from collections import deque
from typing import Optional, List
from BinaryTree import *

# @lc code=start
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return 0

        rs = []
        queue = deque()
        queue.append(root)
        while queue:
            
            levelSum = 0
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            rs.append(levelSum / levelSize)
        
        return rs
# @lc code=end

