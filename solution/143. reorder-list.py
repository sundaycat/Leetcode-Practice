from LinkedList import *

class Solution(LinkedList):

    def reverse(self, head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        
        return pre

    def reorderList(self, head: ListNode) -> None:
        
        # find the midddle node of the linkedlist
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part
        tail = self.reverse(slow)

        # reorder the linkedlist
        rs = head
        while tail.next:

            # save the next head and tail first
            head_next = head.next
            tail_next = tail.next
            
            # reorder, connects the head and tail
            tail.next = head.next
            head.next = tail
            
            # move head and tail forward
            tail = tail_next
            head = head_next

        return rs

values = [1, 2, 3, 4, 5]
s = Solution(values)
s.reorderList(s.head)
s.print_list()