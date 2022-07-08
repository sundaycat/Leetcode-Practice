#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
from typing import Optional
from BinaryTree import *

# @lc code=start

class Solution:
    
    # Solution 1
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = [0]
        self.helper(root, 0, total)
        return total[0]


    def helper(self, node, pathNum, total):

        if node is None:
            return 0
        
        pathNum = pathNum * 10 + node.val
        if node.left is None and node.right is None:
            total[0] += pathNum
        
        self.helper(node.left, pathNum, total)
        self.helper(node.right, pathNum, total)

    # Solution 2: Optimized
    def sumNumbers2(self, root: Optional[TreeNode]) -> int:

        return self.helper2(root, 0)

    def helper2(self, node, pathNum):

        if node is None:
            return 0
        
        pathNum = pathNum * 10 + node.val
        if node.left is None and node.right is None:
            return pathNum
        
        lt = self.helper2(node.left, pathNum)
        rt = self.helper2(node.right, pathNum)

        return  lt + rt
        

        
# @lc code=end

root = [4, 9, 0, 5, 1]
#root = [0, 1]
bst = BinarySearchTree()
bst.insert_level_order(root)
print(bst.pre_order())
s = Solution()
print(s.sumNumbers2(bst.get_root()))

