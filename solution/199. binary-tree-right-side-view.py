#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
from collections import deque
from typing import List, Optional
from BinaryTree import *

# @lc code=start

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []
        
        rs = []
        queue = deque()
        queue.append(root)
        while queue:

            levelSize = len(queue)
            for i in range(levelSize):
                
                node = queue.popleft()
                
                # if it is the last node of the level, add it to the result.
                if i + 1 == levelSize:
                    rs.append(node.val)

                # insert the children of the current node to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return rs

# @lc code=end

root = [1,2,3,None,5,None,4]
root = [1]
root = []

bst = BinarySearchTree()
bst.insert_level_order(root)

s = Solution()
rs = s.rightSideView(bst.get_root())
print(rs)

