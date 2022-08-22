# Definition for singly-linked list.
class ListNode:
    def __init__(self, x = 0):
        self.val = x
        self.next = None

    def __lt__(self, others):
        return self.val < others.val

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

    def print(self, head):

        cur, prefix, rs = head, '', ''
        while cur is not None:
            
            rs += prefix + str(cur.val)
            cur = cur.next

            prefix = ', '
            
        print(rs)
    
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