
from collections import deque
from BinaryTree import *

'''
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
'''
class Solution(object):
    
    def levelOrderSuccessor(self, root: TreeNode, key:int) -> int:

        if not root: return None

        queue = deque()
        queue.append(root)
        while queue:
            '''
            We will not keep track of all the levels. Instead we will keep inserting child nodes to the queue. As sson as we find the given node, we will return the next node from the queue as the level order successor.
            '''
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if node.val == key: break
            
        return queue[0].val if queue else None


s = Solution()
bst = BinarySearchTree()

root = [1, 2, 3, 4, 5, None, None]
root = [1]
bst.insert_level_order(root)

print(bst.pre_order())
rs = s.levelOrderSuccessor(bst.get_root(), 0)
print(rs)