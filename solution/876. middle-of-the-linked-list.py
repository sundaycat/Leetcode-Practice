from LinkedList import *

class Solution(LinkedList):

    def middleNode(self, head:ListNode) -> ListNode:

        fast = slow = head
        # fast for number of nodes being even, and fast.next for odd.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

values = []
s = Solution(values)
mid = s.middleNode(s.head)
print(mid.val)