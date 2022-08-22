from heapq import *

'''
1. add all ropes to the minheap
2. pop out and conenct the two smallest ropes.
3. inserting the resultant rope back in the heap
4. keep track of all cost
'''
def ConnectRope(ropes):

    minHeap = []
    
    # add all ropes to the minheap
    for rope in ropes:
        heappush(minHeap, rope)
    
    curCost, total = 0, 0
    while len(minHeap) > 1:
        
        # pop out and connect the two smallest ropes
        curCost = heappop(minHeap) + heappop(minHeap)

        # keep track of total cost
        total += curCost

        # keep pushing the current cost to minheap util only one element left(result)
        heappush(minHeap, curCost)

    return total

print("Minimum cost to connect ropes: " + str(ConnectRope([1, 3, 11, 5])))
print("Minimum cost to connect ropes: " + str(ConnectRope([3, 4, 5, 6])))
print("Minimum cost to connect ropes: " + str(ConnectRope([1, 3, 11, 5, 2])))