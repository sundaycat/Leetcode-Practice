#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
from collections import deque
from typing import Optional
from BinaryTree import *

# @lc code=start
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        maxDepth = 0
        queue = deque()
        queue.append(root)
        while queue:

            maxDepth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return maxDepth

# @lc code=end


root = [3,9,20,None,None,15,7]
root = [1, None, 2]
root = []
bst = BinarySearchTree()
bst.insert_level_order(root)

s = Solution()
rs = s.maxDepth(bst.get_root())
print(rs)

