'''
Input: [3, -1, 4, 5, 5], k=3, Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

range of index: 0 ~ n - 1
range of values: -infinity ~ infinity

Lets understand this with an example: nums: [2, 1, 3, 6, 5], k =2. After the cyclic sort our array will look like: nums: [1, 2, 3, 6, 5]. From the sorted array we can see that the first missing number is 4 (as we have 6 on the fourth index) but to find the second missing number we need to remember that the array does contain 6. Hence, the next missing number is 7.
'''
def find_first_k_missing_positive(nums, k):

    extra_nums = set()
    i, rs = 0, []
    while i < len(nums):

        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and i != j and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            # while sorting the array, we ignore all numbers that are greater than the array length.
            # However, those ignored numbers could possibly be some of the additional numbers.
            if nums[i] > len(nums):
                extra_nums.add(nums[i])
            i += 1
    
    for i in range(len(nums) + k):
        
        if k == 0: break

        # find the missing positive that greater than the array length and 
        if i >= len(nums) and i + 1 not in extra_nums:
            rs.append(i + 1)
            k -= 1
        
        # find the missing positive that less than the array length
        if i < len(nums) and i != nums[i] - 1:
            rs.append(i + 1)
            k -= 1

    return rs

nums = [3, -1, 4, 5, 5]
nums = [2, 3, 4]
k=3
print(find_first_k_missing_positive(nums, k))