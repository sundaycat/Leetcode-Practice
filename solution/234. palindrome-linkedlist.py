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

    def isPalindrome(self, head: ListNode) -> bool:

        if not head: return False

        # find the middle of the LinkedList
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the the second-half the List
        second_half = self.reverse(slow)
        copy_second_half = second_half

        # compare the first half with second half linkedlist to see if the list is isPalindrome
        while second_half:

            if head.val != second_half.val:
                # restore the linkedlist
                self.reverse(copy_second_half)
                return False
            
            head = head.next
            second_half = second_half.next

        # reverse the second half linkedlist again to bring it back to its original form
        self.reverse(copy_second_half) 
        return True
    
s = Solution([1])
s.print_list()
print(s.isPalindrome(s.head))
s.print_list()