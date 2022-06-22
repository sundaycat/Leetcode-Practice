#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
from typing import Optional
from LinkedList import *

# @lc code=start
class Solution:

    def rotateRight(self, head: Optional[ListNode], rotations: int) -> Optional[ListNode]:

        if head is None or head.next is None or rotations <= 0:
            return head

        # find list length and tail node
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        # rotate the linkedlist, (rotations % length) is the effective number of rotations
        pos = length - (rotations % length)
        new_tail = head
        while pos > 1:
            new_tail = new_tail.next
            pos -= 1

        # conects the tail with head first
        tail.next = head

        head = new_tail.next
        new_tail.next = None

        return head

# @lc code=end

