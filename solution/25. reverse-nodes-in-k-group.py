#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
from typing import Optional
from LinkedList import *

# @lc code=start
class Solution:

    def reverseBetween(self, head, left, right):
         
        idx = 1
        pre, cur = None, head
        while cur and idx < left:
            idx += 1
            pre = cur
            cur = cur.next

        (rev_pre, rev_cur) = self.reverse(pre, cur, left, right)
        
        cur.next = rev_cur
        if pre is not None:
            pre.next = rev_pre
        else:
            head = rev_pre
        
        return head


    def reverse(self, pre, cur, left, right):

        while cur and left <= right:
            
            left += 1
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return (pre, cur)                

         
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # find the total length of the linked list
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        
        # i repreent the number of reverse time, which is less than the total number of k groups
        # number of total k groups = n // k 
        i = 0
        while i < n // k:
            # get the range of index for each sub group.
            left = k * i + 1
            right = k * i + k
            head = self.reverseBetween(head, left, right)
            i += 1
        
        return head
    
    # optimze the solution
    def reverseKGroupOPT(self, head, k):

        count, it = 0, head
        while it:

            count += 1
            it = it.next # save the next link first as it may be cut off after reverse
            if count % k == 0:
                left = count - k + 1
                right = count
                head = self.reverseBetween(head, left, right)
        
        return head
            



# @lc code=end

nums = [1,2,3,4,5,6,7,8,9,10]
#nums = [1,2,3,4,5]
s = Solution()
linklist = LinkedList(nums)
linklist.head = s.reverseKGroup(linklist.head, 3)
linklist.print(linklist.head)