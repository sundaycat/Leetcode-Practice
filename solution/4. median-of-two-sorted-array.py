'''
1. binary search
2. definition median make sure that |#left - #right| <= 1
'''
def find_median_of_two_array(arr1, arr2):

    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    total = len(arr1) + len(arr2)
    half = total // 2

    left, right = 0, len(arr1) - 1
    while True:
        i = (left + right) // 2         # arr1, the mid point of arr1
        j = half - (i + 1) - 1          # arr2, transfer the lenght to index: 一半的长度 - arr1前半段长度 - 1

        l_arr1 = arr1[i] if i >= 0 else float('-infinity')
        r_arr1 = arr1[i+1] if i < len(arr1) - 1 else float('infinity')
        l_arr2 = arr2[j] if j >= 0 else float('-infinity') 
        r_arr2 = arr2[j+1] if j < len(arr2) - 1 else float('infinity')

        if l_arr1 <= r_arr2 and l_arr2 <= r_arr1:

            if total % 2 == 0:
                return (max(l_arr1, l_arr2) + min(r_arr1, r_arr2)) / 2
            
            # 两个数组总长度为奇数时, 把数组一分为二, 后半段总比前半段多出一个元素. 前半段长度: (2n + 1) // 2 = n, 后半段长度: (2n + 1) - n = n + 1
            # 所以median 在后半段中
            return min(r_arr1, r_arr2)

        elif l_arr1 > r_arr2:
            right = i - 1
        
        else: # r_arr1 < l_arr2
            left = i + 1

# l_arr1 > r_arr2, have to shorten the left part of array 1
arr1 = [1, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# r_arr1 < l_arr2, have to shorten the right part of array 1
arr1 = [1, 2, 3, 4]
arr2 = [1,2,3,4,5,6,7,8]