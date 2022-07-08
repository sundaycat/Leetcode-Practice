from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:

    def connectAllSiblings(self, root):

        queue = deque()
        queue.append(root)
        while queue:
            
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            # if the next node exist, link the current with it.
            # if it is the current node is the tail node, set its next to None.
            if not queue:
                node.next = None
            else:
                node.next = queue[0]

        return root