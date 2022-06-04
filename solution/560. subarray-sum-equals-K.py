# https://www.youtube.com/watch?v=fFVZt-6sgyo
# broute force
def subarraySum(nums, k):

    count = 0
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i, len(nums)):
            sub_sum += nums[j]
            if sub_sum == k:
                count += 1

    return count


# sliding window, only applys to positive numbers(No zero) case
def subarray_sum(arr, k):

    if k < arr[0]:
        return 0

    count, sub_sum = 0, 0
    start, end = 0, 0 
    for end in range(start, len(arr)):
        sub_sum += arr[end]
        while sub_sum >= k:   
            if sub_sum == k:
                count += 1             
            sub_sum -= arr[start]
            start += 1

    return count

# prefix sum + hashmap
def subarraySum(nums, k):
    
    # prefix_sum count, by default we have 
    prefix_sum = {0 : 1}
    sub_sum, count = 0, 0
    for i in range(len(nums)):
        sub_sum += nums[i]
        diff = sub_sum - k
        
        # check if the prefix sum exist the sum equals diff
        count += prefix_sum.get(diff, 0)
        
        # increase the count for the cur observed sum
        prefix_sum[sub_sum] = 1 + prefix_sum.get(sub_sum, 0)
    
    return count


nums=[0,1,2,3]
#nums=[1,-1,0]
#nums = [1,1,1]
print(subarray_sum(nums, 0))

