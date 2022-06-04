# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):

    def __init__(self, vals):

        if len(vals) > 0:
            val = vals[0]
            self.node = ListNode(val)
            self.head = self.node
            for i in vals[1:]:
                self.insert_nodes(i)
        else:
            return None


    def print_list(self):
        
        cur = self.head
        while cur is not None:
            print(cur.val, end = ', ')
            cur = cur.next
        print()
    
    def insert_nodes(self, val):

        tail = self.get_tail(self.head)
        tail.next = ListNode(val)

    def get_tail(self, start):
        if start is None or start.next is None:
            return start

        current = start
        while current.next is not None:
            current = current.next

        return current