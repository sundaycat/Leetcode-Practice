#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# @lc code=start

from typing import List, Optional
from LinkedList import *
from heapq import *

# reference: https://www.youtube.com/watch?v=kpCesr9VXDA
class Solution:

    '''
    Solution 1: min heap, O(nlogk), where n is the nnumber of nodes and k is number of list
        1. push the first node of each linkedlist into a min heap.
        2. pop out the smallest(top) node from the heap and links it to the merged list.
        3. push the next element of the same list into the min heap.
        4. continue 2, 3 until the heap is empty
    Note, the lt operator is overloaded in the ListNode.
    '''
    def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # put the first node of each linked list to form a min heap of size k
        minHeap = []
        for i in range(len(lists)):
            node = lists[i]
            heappush(minHeap, node)
        
        dummy = cur = ListNode()
        while minHeap:
            
            node = heappop(minHeap)
         
            # linked the current node to resultant linkedlist and move the cur to next
            cur.next = node
            cur = cur.next

            # push next node in the current linkedlist to the heap
            if node.next:
                # save the current node's next and set it to None
                heappush(minHeap, node.next)

        return dummy.next


    '''           
    Solution 2: divide and conquer, O(nlogk)
    1. divide: recursively divide the array of linkedlist into subllist.
    2. conquer: apply merge sort to the subarrays
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        return self.helper(lists, 0, len(lists) - 1)
    
    def helper(self, lists, start, end):

        # base case, return the node itself when linkedlist length is 1
        if end - start + 1 == 1:
            return lists[start]
        
        # find the linkedlist in the middel of the arrary. 
        mid = (end + start) // 2

        # recursively divide the linkedlist array into subarrays.
        l1 = self.helper(lists, start, mid)
        l2 = self.helper(lists, mid + 1, end)

        # merger two linkedlist together and return.
        return self.mergeTwoList(l1, l2)


    def mergeTwoList(self, head1, head2):

        idx1, idx2 = head1, head2
        
        # use dummy node to avoid comparing head node at the very beginning.
        dummy = cur = ListNode()
        while idx1 and idx2:

            if idx1.val < idx2.val:
                cur.next = idx1
                idx1 = idx1.next
            else:
                cur.next = idx2
                idx2 = idx2.next
            
            cur = cur.next
        
        if idx1:
            cur.next = idx1
        if idx2:
            cur.next = idx2

        return dummy.next


# @lc code=end

# l1 = LinkedList([1,4,5]).head
# l2 = LinkedList([1,3,4]).head
# l3 = LinkedList([2,6]).head

l1 = None

l2 = ListNode(-1)
l2.next = ListNode(5)
l2.next.next = ListNode(11)

l3 = None

l4 = ListNode(6)
l4.next = ListNode(10)

head = Solution().mergeKLists([l1, l2, l3, l4])
res = []
while head:
    res.append(str(head.val))
    head = head.next
print(', '.join(res))

x = None
y = [1,2,3]
z = [x, y]
print(z)
print(len(z))