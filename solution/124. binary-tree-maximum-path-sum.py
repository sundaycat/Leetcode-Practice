#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
import math
from typing import Optional
from BinaryTree import *

# @lc code=start
class Solution:

    '''
    1. keep track of max path sum without spliting for each level
    2. keep track of the global max path sum
    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # 左边, 右边, 左边+右边, 三种情况哪个最大.
        # maxPathSum = [-math.inf]
        # self.helper(root, maxPathSum)
        # return maxPathSum[0]

        pathSum, rs = self.helper2(root)
        return rs

    # Solution using global variable
    def helper(self, node, maxPathSum):

        # base case, handle case like only half substree is None
        if node is None:
            return 0
        
        leftPath = self.helper(node.left, maxPathSum)
        rightPath = self.helper(node.right, maxPathSum)

        leftPath = max(leftPath, 0)
        rightPath = max(rightPath, 0)

        pathSum = max(leftPath, rightPath) + node.val
        maxPathSum[0] = max(maxPathSum[0], leftPath + rightPath + node.val)
 
        return pathSum

    # Solution without global variable
    def helper2(self, node):

        if node is None:
            return (0, -math.inf)
        
        leftPath, leftMax = self.helper2(node.left)
        rightPath, rightMax = self.helper2(node.right)

        leftPath = max(leftPath, 0)
        rightPath = max(rightPath, 0)

        pathSum = max(leftPath, rightPath) + node.val
        maxPathSum = max(leftMax, rightMax, leftPath + rightPath + node.val)

        return (pathSum, maxPathSum)

# @lc code=end

'''
            80
          /    \
        9       20
               /   \
             15     7
'''
# root = [80, 9, 20, None, None, 15, 7]
# root = [-80, 9, -20, None, None, -15, -7]
# root = [2, -1]
# root = [2, -1, -2]
# root = [-1, -5, -2]
root = [-3]

bst = BinarySearchTree()
bst.insert_level_order(root)
print(bst.pre_order())

s = Solution()
print(s.maxPathSum(bst.get_root()))