#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
from typing import Optional
from LinkedList import *

# @lc code=start
class Solution:
    
    '''
    1. Find the list length and the tail node
    2. calcuate the effective number of rotations and find the position of new list's tail node.
    3. reconect the node to form the new rotated linkedlist.
    '''
    def rotateRight(self, head: Optional[ListNode], rotations: int) -> Optional[ListNode]:

        if head is None or head.next is None or rotations <= 0:
            return head

        # find list length and tail node, 下面的写法保证了, 在得出链表长度的同时, 指针停在链表尾部
        length, tail = 0, head
        while tail.next:
            length += 1
            tail = tail.next
        length += 1

        # rotate the linkedlist, (rotations % length) is the effective number of rotations
        # locate the new head and tail position.
        pos = length - (rotations % length)
        new_tail = head
        while pos > 1:
            new_tail = new_tail.next
            pos -= 1

        # reconect the node to form the new rotated linkedlist.
        tail.next = head
        head = new_tail.next
        new_tail.next = None

        return head

# @lc code=end

nums = [1,2,3,4,5]
link = LinkedList(nums)
s = Solution()
head = s.rotateRight(link.head, 5)
link.print(head)

