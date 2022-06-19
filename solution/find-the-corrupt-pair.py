'''
We are given an unsorted array containing nnumbers taken from the range 1 to n. The array originally contained all the numbers from 1 to n, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Input: [3, 1, 2, 5, 2], Output: [2, 4]. Explanation: '2' is duplicated and '4' is missing.

range of index: 0 ~ n - 1 
range of value: 1 ~ n
'''

def find_corrupt_numbers(nums):

    i, rs = 0, []
    while i < len(nums):

        j = nums[i] - 1
        if i != j and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    print(nums)
    for i in range(len(nums)):
        if i != nums[i] - 1:
            rs.extend([nums[i], i + 1])

    return rs

nums = [3, 1, 2, 5, 2]  # 2, 4
nums = [3, 1, 2, 3, 6, 4] # 3, 5
nums = [3, 1, 2, 2, 3, 6]
print(find_corrupt_numbers(nums))