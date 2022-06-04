# median: * *
#         ^ 
#         * * *
#           ^
# 左闭右开, return the median index of current subarray
def find_median(arr, start, end):
    
    if not arr or len(arr) == 1:
        return arr
    
    for i in range(start + 1, end):

        num = arr[i]
        for j in range(i, -1, -1):

            if j <= start or num > arr[j-1]:
                arr[j] = num
                break

            arr[j] = arr[j-1]

    return (end + start - 1) // 2


# return the index of the median in current subarray
def partition(arr, start, end, median):

    arr[start], arr[median] = arr[median], arr[start]
    i = start + 1
    for j in range(start + 1, end, 1):
        if arr[j] < arr[start]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i-1], arr[start] = arr[start], arr[i-1]
    return i - 1


# median of medians, 左闭右开, end doesn't include
# it takes O(n) time since every round we force the algorithm to run with a good pivot
def select(arr, start, end, rank):

    if end - start == 1:
        return start

    # 1. diveide the n elements into groups of 5. find the median of each 5-element group
    sub_lt, sub_rt = 0, 0
    num_of_medians = (end - start) // 5 if (end - start) % 5 == 0 else (end -start) // 5 + 1
    for i in range(num_of_medians):

        # 左闭右开
        sub_lt = start + 5*i
        sub_rt = start + 5*(i+1) if start + 5*(i+1) < end else end

        # find the median(index) of each five-elements groups
        median = find_median(arr, sub_lt, sub_rt)

        # move the medians of five-elements groups to the first n/5 position of the subarray
        arr[start + i], arr[median] = arr[median], arr[start + i]

    # 2. recursively select the median x of the n/5 group medians to be the pivot
    median_of_medians = select(arr, start, start + num_of_medians, (start + num_of_medians + 1) // 2)
    
    # 3. partition around the meidan of medians given above
    pivot_idx = partition(arr, start, end, median_of_medians)

    # 4. recursively invoke select function to find the target rank. 
    cur_rank = pivot_idx - start + 1
    if rank == cur_rank:
        return pivot_idx
    else:
        if rank < cur_rank:
            # 左闭右开, 不包括pivot
            return select(arr, start, pivot_idx, rank)
        else:
            return select(arr, pivot_idx+1, end, rank - cur_rank)


# arr = [0,1,2,3,4,5,6,7,8,9,10]
arr = [1,3,5,2,4,8,9,10,7,6,0]
# arr = [0, 1]
x = select(arr, 0, len(arr), 5)
print(arr[x])