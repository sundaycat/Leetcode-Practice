from random import randrange
'''
Q: Given an unsorted array, find its kth smallest elements O(N)

Solution: 
Step 1: Apply the selection algorithm that we applied in quick sort
Step 2: Recursively compare the K-rand with current pivot's rank and which half the K-rand exist and keep searching until
        the k-rank is found. 
Ex:
ranks 1  2  3  4  5  6  7  8
index 0  1  2  3  4  5  6  7
value 2  3  5  6  8 10 11 13
'''
# k: is the rank of the element in the array
# start: is the starting index of the array
# end: = len(arr) + 1
def find_kth_element(arr, k, start, end):

    # corner case
    if start == end: return arr[start]

    # randomly pick up the pivot index and switch its value with start-th element
    pivot = randrange(start, end)
    arr[start], arr[pivot] = arr[pivot], arr[start]

    # divide the array into to smaller half and larger half based on the value of pivot-th element
    i = start
    for j in range(start + 1, end):
        if arr[j] < arr[start]:
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            i += 1
    arr[start], arr[i] = arr[i], arr[start]

    # calculate the rank of current pivot element in Array[start:end]
    rank = i - start + 1
    if rank == k:
        return arr[i]
    elif rank < k:
        # (k - rank) gives the rank of the kth element in the new Array[i+1, end]
        return find_kth_element(arr, k - rank, i + 1, end)
    else:
        return find_kth_element(arr, k, start, i)


arr1 = [6,10,13,5,8,3,2,11]
print(find_kth_element(arr1, 3, 0, len(arr1)))
