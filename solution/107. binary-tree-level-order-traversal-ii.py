#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
from collections import deque
from typing import Optional, List
from BinaryTree import *
# @lc code=start

class Solution:

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        # use deque to save the result
        rs = deque()
        queue = deque()
        queue.append(root)
        while queue:

            curLevel = []
            for i in range(len(queue)):
                node = queue.popleft()
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.appendleft(curLevel)
        
        return rs

# @lc code=end

root = [3,9,20,None,None,15,7]
bst = BinarySearchTree()
bst.insert_level_order(root)

s = Solution()
rs = s.levelOrderBottom(bst.get_root())
print(rs)

