from LinkedList import *
'''
在python 判断语句中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于 False 
not None == not False == not '' == not 0 == not [] == not {} == not ()
'''
class Solution(LinkedList):

    def hasCycle(self, head: ListNode) -> bool:

        if not head: return False
        
        slow, fast = head, head
        while fast.next and fast.next.next:

            if slow == fast:
                return True

            fast = fast.next.next
            slow = slow.next

        return False

vals = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]

s = Solution(vals)
s.print_list()
print(s.hasCycle(s.head)) # should be False