#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
from collections import deque
from typing import Optional

# Definition for a Node.
class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# perfect binary tree
class Solution:

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root: return None

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
            
                # 1. i + 1 == level_size: node = queue.popleft(); node.next = None
                # 2. i + 1 <  level_size: node = queue.popleft(); node.next = queue[0]
                if i == levelSize - 1:
                    node.next = None
                else:
                    node.next = queue[0]
            
        return root
            
# @lc code=end

