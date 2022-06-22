#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
from LinkedList import *

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # always save the link beofore we dicard it.
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        
        return pre
        
# @lc code=end

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testList = LinkedList(nums)
s = Solution()
new_head = s.reverseList(testList.head)

testList.print(new_head)