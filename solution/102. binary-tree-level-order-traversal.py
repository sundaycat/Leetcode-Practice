#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from collections import deque
from typing import List, Optional
from BinaryTree import *

# @lc code=start
'''
1. Start by pushing the root node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, 
    3.1 First count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
    3.2 Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
4. After removing each node from the queue, insert both of its children into the queue.
5. If the queue is not empty, repeat from step 3 for the next level.
'''
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root
        
        rs = []
        queue = deque()
        queue.append(root)
        while queue:

            curLevel = []
            for i in range(len(queue)):

                node = queue.popleft()
                curLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            rs.append(curLevel)

        return rs            

# @lc code=end

root = [3,9,20,None,None,15,7]
root = [3,9,20,4,5,15,7]

bst = BinarySearchTree()
bst.insert_level_order(root)

s = Solution()
rs = s.levelOrder(bst.get_root())
print(rs)

print(bst.pre_order())
