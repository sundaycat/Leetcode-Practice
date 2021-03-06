from random import randrange
#from medianOfMedians import select

'''
start: the starting point of the sub-array 
end: the ending point of the sub-array. End = len(sub-array). [start, end)
pivot: the index of the pivot element.
'''
def partition(arr, start, end):

    # randomly pick the pivot index
    pivot = randrange(start, end)
    # pivot = select(arr, start, end, (end+start)//2)

    # swap pivot to the first element of the array
    arr[start], arr[pivot] = arr[pivot], arr[start]
    i = start
    # "end" would not be included in the range of j
    for j in range(start + 1, end):
        if arr[j] < arr[start]:
            # find the element that larger than pivot and swap them with the (i + 1)th element
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            i += 1

    # swap the pivot with last element that smaller than pivot.
    arr[i], arr[start] = arr[start], arr[i]
    return i


# end is one larger than the index of last element, end-th element would not be involved during sorting
def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot)
        quick_sort(arr, pivot + 1, end)


# test case
test = [4, 2, 7, 2, 3, 9, 10, 1, 21, 18, 96, 21, 13]
quick_sort(test, 0, len(test))
print(test)
