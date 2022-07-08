#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
from collections import deque
from typing import Optional, List
from BinaryTree import *

# @lc code=start
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        # keep track of levels and determine whether or not switch the transversing direction
        # direction = 1
        rs, level = [], 0
        queue = deque()
        queue.append(root)
        while queue:
            
            curLevel = deque()
            for i in range(len(queue)):

                node = queue.popleft()

                # add the node to the current level based on the traverse direction
                if level % 2 == 0:
                    curLevel.append(node.val)
                else:
                    curLevel.appendleft(node.val)

                # insert the children of current node in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # reverse the traversal direction
            level += 1
            # direction = not direction
            rs.append(curLevel) 

        return rs       

# @lc code=end


root = [3,9,20,None,None,15,7]
bst = BinarySearchTree()
bst.insert_level_order(root)
s = Solution()
print(s.zigzagLevelOrder(bst.get_root()))