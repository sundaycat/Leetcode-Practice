# brute force
def find_max_subarray_1(arr):

    max_sub = float('-inf ')
    start, end = 0, 0
    for i in range(0, len(arr)):
        sum_of_sub = 0
        for j in range(i, len(arr)):
            sum_of_sub += arr[j]
            if max_sub < sum_of_sub:
                max_sub = sum_of_sub
                start = i
                end = j

    return arr[start:end+1]

# divide and conquer, 左闭右闭
def find_max_subarray_2(arr, start, end):

    if start == end:
        return arr[start]

    mid = (start + end) // 2
    l_max = find_max_subarray_2(arr, start, mid)
    r_max = find_max_subarray_2(arr, mid + 1, end)
    cross_max = find_max_cross_subarray(arr, start, end)

    return max(l_max, r_max, cross_max)

def find_max_cross_subarray(arr, start, end):

    mid = (start + end) // 2
    l_sum, l_max = 0, float('-inf')
    for i in range(mid, start - 1, -1):
        l_sum += arr[i]
        if l_max < l_sum:
            l_max = l_sum

    r_sum, r_max = 0, float('-inf')
    for i in range(mid + 1, end + 1):
        r_sum += arr[i]
        if r_max < r_sum:
            r_max = r_sum

    return l_max + r_max

# Dynamic programing
def find_max_subarray_3(arr):
    # cur_max denote the current max subarray ending at index i
    # glb_max denote the global max subarray among all possible subarray
    cur_max = glb_max = float('-inf')
    for i in range(0, len(arr)):
        # the cur_max(i) is either ith element itself or previous max plus ith max.
        cur_max = max(arr[i], cur_max + arr[i])
        if cur_max > glb_max:
            glb_max = cur_max

    return glb_max

# reference：
#   1. https://www.youtube.com/watch?v=86CQq3pKSUw
#   2. https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/


test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test = [2, 3, 4, 5, 7]
print(find_max_subarray_2(test, 0, len(test) - 1))
print(find_max_subarray_3(test))
