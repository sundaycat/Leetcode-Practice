# Dummy node, Resursion
# carry must be either 0 or 1 because the largest possible of two digit(inclduing the carry) is 9 + 9 + 1 = 19

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # solution 1: recursion
    def add_two_numbers_1(self, l1, l2):

        return self.helper(l1, l2, 0)

    def helper(self, l1, l2, carry):

        # ending condition
        if not l1 and not l2 and carry == 0:
            return None

        # if the next node doesn't exist, set the corresponding val to 0
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # calculate the current digit and carry for next digit
        cur_sum = v1 + v2 + carry
        node = ListNode(cur_sum % 10)
        carry = cur_sum // 10

        # update the list pointer, if the list has already been at the end, then do nothing
        l1_next, l2_next = None, None
        if l1:
            l1_next = l1.next
        if l2:
            l2_next = l2.next
        node.next = self.helper(l1_next, l2_next, carry)

        return node

    # solution 2: use dummy node to make code simpler
    def add_two_numbers_2(self, l1, l2):

        dummy = cur = ListNode(None)
        carry = 0
        while l1 or l2 or carry != 0:

            # if the next node doesn't exist, set the corresponding value to 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # calculate the current digit and carry for next digit
            cur_sum = v1 + v2 + carry
            cur.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10

            cur = cur.next

            # if the list is not empty, move to the next node
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

    
    def add_two_numbers_3(self, l1, l2):

        head, l3 = None, None
        adder, val = 0, 0
        while l1 and l2:
            
            total = l1.val + l2.val + adder
            val = total % 10
            adder = total // 10
             
            if not l3:
                l3 = ListNode(val)
                head = l3
            else:
                l3.next = ListNode(val)
                l3 = l3.next
            
            l1 = l1.next
            l2 = l2.next
        
        # 999, 99 
        while l1:
            val = (l1.val + adder) % 10
            adder = (l1.val + adder) // 10
            l3.next = ListNode(val)
            l3 = l3.next
            l1 = l1.next
            
        while l2:
            val = (l2.val + adder) % 10
            adder = (l2.val + adder) // 10
            l3.next = ListNode(val)
            l3 = l3.next
            l2 = l2.next
            
        if adder != 0:
            l3.next = ListNode(adder)
        
        return head


x = [2, 4, 3]
y = [5, 6, 4]
# x = [4, 9, 9]
# y = [8]

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l2 = ListNode(9)

s = Solution()
l3 = s.add_two_numbers_1(l1, l2)

cur = l3
prefix, list_str = '', ''
while cur:
    list_str += prefix + str(cur.val)
    prefix = ' '
    cur = cur.next
print(list_str)