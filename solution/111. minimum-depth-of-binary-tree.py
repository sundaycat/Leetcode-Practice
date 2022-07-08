#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
from collections import deque
from typing import Optional
from BinaryTree import *

# @lc code=start
class Solution:

    '''
    return when encounter the first leaf node.
    '''
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        queue = deque()
        queue.append(root)

        minDepth = 0
        while queue:

            # increase the Depth by one for the current level
            minDepth += 1
            for _ in range(len(queue)):

                node = queue.popleft()

                # check if this is a leaf node
                if not node.left and not node.right:
                    return minDepth
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
# @lc code=end

s = Solution()
bst = BinarySearchTree()

root = [3,9,20,None,None,15,7]
bst.insert_level_order(root)
print(bst.pre_order())
print(s.minDepth(bst.get_root()))
 