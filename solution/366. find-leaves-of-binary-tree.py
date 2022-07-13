
from typing import List
from BinaryTree import *

'''
reference:  https://www.youtube.com/watch?v=zwCZU5XGtnY
            https://leetcode.ca/all/366.html
'''         
class Solution:

    def find_leaves(self, root: TreeNode) -> List[List]:

        # Solution 1: O(NlogN)
        # rs = []
        # while root.left or root.right:
        #     leaves = []
        #     self.helper(root, leaves)
        #     rs.append(leaves)
        # rs.append([root.val])
        # return rs

        # Solution 2: O(N)
        rs = []
        self.getHeight(root, rs)
        return rs

    # Solution 1
    def helper(self, node, leaves):

        if node is None:
            return False
        
        if node.left is None and node.right is None:
            leaves.append(node.val)
            return True

        left = self.helper(node.left, leaves)
        right = self.helper(node.right, leaves)

        if left:
            node.left = None
        if right:
            node.right = None
        
        return False

    # Solution 2: process tree and count the tree height bottom up
    def getHeight(self, node, rs):
        
        if node is None:
            return -1
        
        # traverse the left and right subtree.
        leftHeight = self.getHeight(node.left, rs)
        rightHeight = self.getHeight(node.right, rs)

        # calcuate the current height
        curHeight = max(leftHeight, rightHeight) + 1
        
        # if a new height found, append a new list into the rs.
        if curHeight >= len(rs):
            rs.append([])
        rs[curHeight].append(node.val)

        # invariance: alway return the current depth to its upper level.        
        return curHeight
         

'''
                1
              /   \
            2      3
          /   \
         4     5
'''
root = [1,2,3,4,5]
bst = BinarySearchTree()
bst.insert_level_order(root)

s = Solution()
rs = s.find_leaves(bst.get_root())
print(rs)