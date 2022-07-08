#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
from typing import Optional
from BinaryTree import *

# @lc code=start

class Solution:
    '''
    Invariant: 
        1. path includes nodes in the upper level and current level.
        2. variable count counts the path that meets requirment for this level only.

    Time complexity: O(NlogN) ~ O(N^2)
        visited each node only once during traversing. But for each node, we iterate each path and in the worst case, the path length could be N for a unbalanced tree
    Space complexity: O(N)
    '''
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.helper(root, targetSum, [])

    def helper(self, node, targetSum, path):
        
        if node is None:
            return 0

        # add the current node into the path
        path.append(node.val)

        # find the sums of all sub-paths in the current path list
        pathSum, count = 0, 0
        for i in range(len(path) - 1, -1, -1):
            pathSum += path[i]
            if pathSum == targetSum:
                count += 1
        
        # traverse left and right sub-tree.
        count += self.helper(node.left, targetSum, path)
        count += self.helper(node.right, targetSum, path)

        # restore path to the status of upper level before jumpping back
        path.pop()

        return count


# @lc code=end

root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
targetSum = 8

# root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
# targetSum = 22

bst = BinarySearchTree()
bst.insert_level_order(root)
print(bst.pre_order())

s = Solution()
rs = s.pathSum(bst.get_root(), targetSum)
print(rs)