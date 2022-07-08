## Problem List of DFS ##
---
### **Overview**
This pattern is based on the Breadth First Search (BFS) technique to traverse a tree.

Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a `Queue` to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be O(W), where ‘W’ is the maximum number of nodes on any level.

+ 使用优先队列来实现层级遍历.
+ 是否逐层遍历.

### problem set 1
+ [102. Binary Tree Level Order Traversal][1]
+ [107. Binary Tree Level Order Traversal II][2]
+ [103. Binary Tree Zigzag Level Order Traversal][3]
+ [637. Average of Levels in Binary Tree][4]
    + [515. Find Largest Value in Each Tree Row][5]
+ [111. Minimum Depth of Binary Tree][6]
    + [104. Maximum Depth of Binary Tree][7]
+ [Level Order Successor][8]
+ [116. Populating Next Right Pointers in Each Node][9] - perfect binary tree
    + [117. Populating Next Right Pointers in Each Node II][11] - binary tree
    + Use constant space (recursive approach is fine)


### problem set 2
+ [Connect All Level Order Siblings][10]
+ [199. Binary Tree Right Side View][12]
    + Follow up: find the left side view.

---

[1]: https://leetcode.com/problems/binary-tree-level-order-traversal/
[2]: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
[3]: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
[4]: https://leetcode.com/problems/average-of-levels-in-binary-tree/
[5]: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
[6]: https://leetcode.com/problems/minimum-depth-of-binary-tree/
[7]: https://leetcode.com/problems/maximum-depth-of-binary-tree/
[8]: https://www.educative.io/courses/grokking-the-coding-interview/7nO4VmA74Lr
[9]: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
[10]: https://www.educative.io/courses/grokking-the-coding-interview/NE5109Jl02v
[11]: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/ 
[12]: https://leetcode.com/problems/binary-tree-right-side-view/