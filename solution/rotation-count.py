def count_rotations(arr):

    lt, rt = 0, len(arr) - 1
    while lt < rt - 1:
        mid = (lt + rt) // 2
        if arr[lt] <= arr[mid]:
            # left half is sorted, so we look to the right
            lt = mid
        else:
            # right half is sorted, so we look to the left.
            rt = mid
    
    # find the maximum index and minimum is next to it.
    maxIdx = lt if arr[lt] > arr[rt] else rt
    # if the array is completely sorted, return 1st element.
    minIdx = (maxIdx + 1) % len(arr)
    
    return minIdx

arr = [10, 15, 1, 3, 8]

print(count_rotations([10, 15, 1, 3, 8]))
print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
print(count_rotations([1, 3, 8, 10]))
print(count_rotations([4, 5, 6, 7, 0, 1, 2]))
