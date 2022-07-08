 #
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
import binhex
from typing import List, Optional
from BinaryTree import *

# @lc code=start
class Solution:

    '''
    invariant state of each level:(the moment we enter the level) 
        1. path include nodes from root to current node
        2. pathsum = targetsum - upperlevel sum
    '''
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        rs = []
        self.helper(root, targetSum, [], rs)
        return rs
    
    def helper(self, node, pathSum, path, rs):

        if node is None:
            return 
        
        # maintain invariant: add the current node to the path
        path.append(node.val) 

        # if the current node is leaf and its value equals the required sum, save the path      
        if node.val == pathSum and node.left is None and node.right is None:
            rs.append(list(path))
        
        self.helper(node.left, pathSum - node.val, path, rs)
        self.helper(node.right, pathSum - node.val, path, rs)

        # restore the invariant of upper level while going back to the upper level
        path.pop()

# @lc code=end
'''
                5                                           
              /    \
            4       8
          /        /  \
        11       13    4
       /  \             \
      7    2             1
             \
              6
'''
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1, None, None, None, 6]

bst = BinarySearchTree()
bst.insert_level_order(root)
print(bst.pre_order())

s = Solution()
rs = s.pathSum(bst.get_root(), 22)
print(rs)