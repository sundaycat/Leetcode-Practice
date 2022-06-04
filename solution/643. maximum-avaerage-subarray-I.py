def findMaxAverage(nums, k):
    windowSum, windowStart, maxAverage = 0.0, 0, float('-inf')
    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]
        if windowEnd >= k - 1:
            maxAverage = max(maxAverage, windowSum / k)
            windowSum -= nums[windowStart]
            windowStart += 1

    print(maxAverage)


nums = [4,0,4,3,3]
k = 5
print(len(nums))
findMaxAverage(nums, k)

# 需要记录大小的值,在初始化的时候要注意取系统允许的最大,最小值.


def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here
    start, sub_arr = 0, []
    max_sum, sub_sum = float('-inf'), 0.0
    for end in range(len(arr)):
        sub_sum += arr[end]
        if end >= k - 1:
            if sub_sum > max_sum:
                sub_arr = arr[start : end + 1]
                max_sum = sub_sum

            sub_sum -= arr[start]
            start += 1

    return sub_arr


arr = [2, 3, 4, 1, 5, 3]
k = 2
print(max_sub_array_of_size_k(k, arr))