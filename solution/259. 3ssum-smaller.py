'''
Given an array of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Note: If the current triplet sum < target, then, we can replace arr[right] by any number between left and right to get a sum less than the target sum

Time complexity: O(N^2)
'''

def triplet_with_smaller_sum(arr, target):

    arr.sort()

    count = 0
    for i in range(len(arr) - 3 + 1):

        lt, rt = i + 1, len(arr) - 1
        while lt < rt:

            _sum = arr[i] + arr[lt] + arr[rt]
            if _sum < target:
                count += rt - lt
                lt += 1
            else:
                rt -= 1
        
    return count


print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))