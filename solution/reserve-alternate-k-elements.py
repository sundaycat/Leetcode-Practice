
from ast import Lt
from LinkedList import *

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


    def reverseAlternateKElements(self, head: ListNode, k: int) -> ListNode:

        count, cur = 0, head
        while cur:

            # count the current node
            count += 1
            
            # save current node's next node as it may cut off during reversing.
            cur = cur.next

            # count % k == 0 guarntee we only reverse at every k elements
            # (count // k) % 2 guarntee that we reverse k elements alternatively
            if (count % k == 0) and (count // k) % 2 != 0:
                
                lt = count - k + 1
                rt = count
                head = self.reverseBetween(head, lt, rt)
        
        return head

nums = [1, 2, 3, 4, 5, 6]
k = 2

# nums = [1, 2, 3, 4, 5]
# k = 3

nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2

s = Solution()

linkedlist = LinkedList(nums)
linkedlist.head = s.reverseAlternateKElements(linkedlist.head, k)
linkedlist.print(linkedlist.head)