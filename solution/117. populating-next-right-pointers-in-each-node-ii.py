#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
from collections import deque

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Not a perfect binary tree
class Solution:

    def connect(self, root: 'Node') -> 'Node':

        if not root: return root

        queue = deque()
        queue.append(root)
        while queue:
            
            levelSize = len(queue)
            for i in range(levelSize):

                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i + 1 == levelSize:
                    node.next = None
                else:
                    node.next = queue[0]
        
        return root
        
# @lc code=end

