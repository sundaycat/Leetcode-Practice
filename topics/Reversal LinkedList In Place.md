## In-place Reversal Linked list

### **Overview**
In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

+ **key point**: 
    + always save the link before cut it off.
    + create dummpy pre node to avoid corner cases.
    >
        pre     cur     =>
        None -> head

### Problem set 1
+ [206. Reverse Linked List][1]
+ [092. Reverse Linked List II][2]
    + [Q1][3]: Reverse the first ‘k’ elements of a given LinkedList
    + [Q2][3]: Given a LinkedList with ‘n’ nodes, reverse it based on its size in the way
        1. If n is even, reverse the list in a group of n/2 nodes.
        2. If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last n/2 nodes.
+ [025. Reverse Nodes in k-Group][4]

### Problem set 2
+ [Reverse alternating K-element sub_list][5]
+ [61. Rotate List][6]


[1]: https://leetcode.com/problems/reverse-linked-list
[2]: https://leetcode.com/problems/reverse-linked-list-ii
[3]: https://www.educative.io/courses/grokking-the-coding-interview/qVANqMonoB2
[4]: https://leetcode.com/problems/reverse-nodes-in-k-group
[5]: https://www.educative.io/courses/grokking-the-coding-interview/m2YYJJRP9KG
[6]: https://leetcode.com/problems/rotate-list