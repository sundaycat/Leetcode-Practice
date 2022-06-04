import random

# On average, it takes O(n) linear time
random.seed(42)
def partition(arr, start, end):

    pivot = random.randrange(start, end)
    print('pivot: {}'.format(pivot))
    arr[start], arr[pivot] = arr[pivot], arr[start]
    
    i = start + 1
    for j in range(start+1, end, 1):
        if arr[j] < arr[start]:
            arr[j], arr[i] = arr[i], arr[j] 
            i += 1
    arr[start], arr[i-1] = arr[i-1], arr[start]

    # return the pivot index
    return i - 1

# find the indicated rank position of element we are interested.
def select(arr, start, end, find):
    
    pivot = partition(arr, start, end)

    # convert the pivot pos to its corresponding rank in the current subarray
    cur_rank = pivot - start + 1
    if find == cur_rank:
        return arr[pivot]
    else:
        if find < cur_rank:
            # doesn't include pivot
            return select(arr, start, pivot, find)
        else:
            # include pivot
            return select(arr, pivot+1, end, find-cur_rank)


ar1 = [2, 3, 5, 6, 8, 10, 11, 13]
arr = [6, 10, 13, 5, 8, 3, 2, 11]
print(select(arr, 0, len(arr), 6))

