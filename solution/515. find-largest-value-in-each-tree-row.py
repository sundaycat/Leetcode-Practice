#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
import math
from collections import deque
from typing import Optional, List
from BinaryTree import *

# @lc code=start
class Solution:
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []

        rs = []
        queue = deque()
        queue.append(root)
        while queue:
            
            levelMax = -math.inf
            for _ in range(len(queue)):

                # keep track of the max value of the current level
                node = queue.popleft()
                levelMax = max(levelMax, node.val)

                # insert the node of next level to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            rs.append(levelMax)
        
        return rs
        
# @lc code=end

