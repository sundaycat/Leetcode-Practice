'''
Solution 1
'''
def search_floor_of_a_number(arr, key):

    if arr[0] > key:
        return -1

    lt, rt = 0, len(arr) - 1
    while lt <= rt:
    
        mid = (lt + rt) // 2
        if arr[mid] == key:
            return key
        elif arr[mid] < key:
            lt = mid + 1
        else:
            rt = mid - 1

    # by the end, rt == lt - 1 and points to the cloest number to the target
    return rt

'''
Solution 2: Find the left element that is cloest to the key
1. if mid == key, set lt = mid
2. if mid < key, set lt = mid because there could be more element on its right meets requirment.
3. if mid > key, set lt = mid - 1 as the mid doesn't meets requirment and can be removed.
combine 1 and 2.

'''
def search_floor(arr, key):

    lt, rt = 0, len(arr) - 1
    while lt < rt - 1:
        mid= (lt + rt) // 2
        if arr[mid] <= key:
            # k
            lt = mid
        else:
            rt = mid - 1
    
    # postprocessing the last two elements.
    if arr[rt] <= key:
        return rt
    if arr[lt] <= key:
        return lt

    return -1    


 
nums = [1, 3, 8, 10, 15]
key = 5
key = 16
rs = search_floor(nums, key)
print(rs)