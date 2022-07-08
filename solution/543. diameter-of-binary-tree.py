#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

import math
from typing import Optional
from BinaryTree import *

# @lc code=start

'''
Invariant: always return the max height of current node to upper level.
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # maxPathLen = [0]
        # self.helper(root, maxPathLen)
        # return maxPathLen[0] - 1

        return self.helper(root)[1] - 1

    # solution with global variable
    def helper2(self, node, maxPathLen):

        if node is None:
            return 0
        
        ltMaxHeight = self.helper(node.left, maxPathLen)
        rtMaxHeight = self.helper(node.right, maxPathLen)

        # check if whether or not the longest path is
        #   the max height of left subtree + max height of right substree + 1(current node) or
        #   some path in the subtree of current node.
        maxPathLen[0] = (ltMaxHeight + rtMaxHeight + 1, maxPathLen[0])
        
        # return the maximum height of current level to upper level.
        return max(ltMaxHeight, rtMaxHeight) + 1    
    
    # solution without global variable
    def helper(self, node):
        
        if node is None:
            return (0, 0)
        
        ltMaxHeight, ltMaxPath = self.helper(node.left)
        rtMaxHeight, rtMaxPath = self.helper(node.right)

        # max path len of the current node can only come from:
        # 1. the max path of left subtree
        # 2. the max path of right subtree
        # 3. max height of left subtree + max hegiht of right substree + 1
        maxPathLen = max(ltMaxPath, rtMaxPath, ltMaxHeight + rtMaxHeight + 1)

        return (max(ltMaxHeight, rtMaxHeight) + 1, maxPathLen)

# @lc code=end
'''

'''
root = [1,2,3,4,5,None,None]
root = [1,2,3,4,7,None,None,5,None,None,8,None,None,None,None,6,None,None,None,None,None,None,9]

bst = BinarySearchTree()
bst.insert_level_order(root)

s = Solution()
rs = s.diameterOfBinaryTree(bst.get_root())
print(rs)
