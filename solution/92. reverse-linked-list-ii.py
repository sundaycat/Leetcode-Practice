#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II

from typing import Optional
from LinkedList import *
# @lc code=start
'''
Anaysis:
1. use dummpy node
2. linked the reverse list to form a new list.
    2.1 if pre is None, head = rev_pre
    2.2 if pre is not None, pre.next = rev_pre

Follow up:
1. Q: reverse the first K elements
2. Q: reverse first and second half, but keep the middle node
'''
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # find the start of the sublist, cur will stop at the start when loop stops
        idx = 1
        pre, cur = None, head
        while cur and idx < left:
            pre = cur
            cur = cur.next
            idx += 1

        # reverse sublist
        (rev_pre, rev_cur) = self.reverse(pre, cur, left, right)

        # reconect to form a new list
        cur.next = rev_cur
        if pre is not None:
            pre.next = rev_pre
        else:
            head = rev_pre
        
        return head
    
    def reverseHalves(self, head):

        # obtain the length of the linkedlist
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        
        if n % 2 == 0:  # length is even
            head = self.reverseBetween(head, 1, n // 2)
            head = self.reverseBetween(head, n // 2 + 1, n)
        else:           # length is odd
            head = self.reverseBetween(head, 1, n // 2)
            head = self.reverseBetween(head, n // 2 + 2, n)

        return head

    def reverse(self, pre, cur, left, right):

        while cur and left <= right:

            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

            left += 1

        return (pre, cur)
        
# @lc code=end
s = Solution()

# reverse between
nums = [1, 2, 3, 4, 5]
left, right = 2, 4 
# nums = [5]
# left, right = 1, 1
# nums = [3, 5]
# left, right = 1, 2
linklist = LinkedList(nums)
linklist.head = s.reverseBetween(linklist.head, left, right)
linklist.print(linklist.head)

# reverse first k
linklist = LinkedList(nums)
k = 3
linklist.head = s.reverseBetween(linklist.head, 1, k)
linklist.print(linklist.head)

# reverse pre-half and later-half, if it is odd, keep the middle
nums = [1,2,3,4,5]
linklist = LinkedList(nums)
linklist.head = s.reverseHalves(linklist.head)
linklist.print(linklist.head)