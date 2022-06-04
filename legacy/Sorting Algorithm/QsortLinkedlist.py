# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # return True if swap happens, otherwise return false
    def swap(self, pre_outer, outer, pre_mini, mini):

        # 1. mini itself is outer
        # 2. mini and outer is adjacent
        # 3. mini is somewhere else in the linked list
        if outer is mini:
            return False
        elif outer.next == mini:
            outer.next = mini.next
            mini.next = outer
            pre_outer.next = mini
        else:
            temp = mini.next
            pre_outer.next = mini
            mini.next = outer.next
            pre_mini.next = outer
            outer.next = temp

        return True

    # quick sort
    def partition(self, start, end):

        dummy = ListNode(None)
        dummy.next = start

        # initialize pointers
        pre_i, i = dummy, start
        pre_j, j = start, start.next
        while j is not end:

            # if swap happens, set has_swap to True, otherwise set it to False
            has_swap = False
            if j.val < start.val:

                has_swap = self.swap(i, i.next, pre_j, j)

                # move pre_i, i forward
                pre_i = pre_i.next
                i = i.next

                if has_swap:
                    # reset point j after swapping, make it point to next node of pre_j again
                    j = pre_j.next

            # move pre_j, j forward if swapping doesn't occur
            if j is not end and not has_swap:
                pre_j = pre_j.next
                j = j.next

        # swapping the first node(stores the pivot) with the ith node.
        self.swap(dummy, start, pre_i, i)

        # reset start and i after swapping
        pivot = start
        start = i

        return start, pivot

    def quick_sort(self, start, end):

        if start is None:
            return start
        elif start is end:
            return start
        else:
            start, pivot = self.partition(start, end)

            # sorting before and after the pivot position
            l_head = self.quick_sort(start, pivot)
            r_head = self.quick_sort(pivot.next, end)

            # re-connect pivot node to the head of right linked list
            pivot.next = r_head

        return l_head

    def quickSort(self, head):
        
        if not head or head.next is None:
            return head
        
        # Find the tail of the current linkedlist
        cur = head
        while cur.next is not None:
            cur = cur.next

        tail = cur
        head = self.quick_sort(head, tail.next)

        return head