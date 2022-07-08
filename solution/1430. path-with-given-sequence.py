
'''
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

        1                   sequence: [1, 9, 9]     output: true
      /   \
     7     9
         /   \
        2     9

A. general case analysis

    if node.val != sequence[level] and havn't reach the leaf: return False;
    if node.val == sequance[level] and havn't reach the leaf: do nothing
    if node.val != sequence[level] and reach the leaf: return False
    if node.val == sequence[level] and reach the leaf: return True

Merge 1,3 together and ignore case 2, then we have:

    if node.val != sequence[level]: return Fasle
    if node.val == sequence[level] and reach the leaf: return True

B. Corner case analysis: level >= len(sequence)

It would cause list level out of range if the all the elements of the list match the upper level of the tree, but the height is more depth than the length of the sequence.

'''

from BinaryTree import *

def find_path(root, sequence): 
    return helper(root, 0, sequence)

def helper(node, level, sequence):

    # base case: avoid subtress is None.
    if node is None:
        return False

    # Avoid tree height is more depth than seq length or node val doesn't match elements in seq
    if level >= len(sequence) or node.val != sequence[level]:
        return False

    if node.left is None and node.right is None and level == len(sequence) - 1:
        return True

    lt = helper(node.left, level + 1, sequence)
    rt = helper(node.right, level + 1, sequence)

    return (lt or rt)


root = [1, 7, 9, None, None, 2, 9]
root = [1, 2]

bst = BinarySearchTree()
bst.insert_level_order(root)
print(bst.pre_order())

sequence = [1, 9, 9]
sequence = [1, 9]

rs = find_path(bst.get_root(), sequence)
print(rs)