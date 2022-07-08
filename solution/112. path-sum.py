#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
from typing import Optional
from BinaryTree import *

# @lc code=start
class Solution:
    '''
    Invariant of each level: pathSum = targetSum - sum of previous node(no including the current node). 
    '''
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum)
        
    def helper(self, node, pathSum):

        # base case, whenever we reach the end of a path, it means it is not the target path
        if node is None:
            return False

        # if the current node is leaf and its value equals the pathSum, then we found a target path
        if node.left is None and node.right is None and pathSum == node.val:
            return True

        # recursively call to traverse the left and right sub-tree
        # 1. substrct the value of the node from the given pathSum
        # 2. make two recursive calls for left and right sub-stree
        lt = self.helper(node.left, pathSum - node.val)
        rt = self.helper(node.right, pathSum - node.val)

        return (lt or rt)
 
# @lc code=end

''' Target sum = 22
                5
              /    \
            4       8
          /        /  \
        11       13    4
       /  \             \
      7    2             1
'''
root = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,1]
targetSum = 22

bst = BinarySearchTree()
bst.insert_level_order(root)
print(bst.pre_order())

s = Solution()
print(s.hasPathSum(bst.get_root(), 22))