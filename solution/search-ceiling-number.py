'''
Assume there exist duplicats numbers.

1. locate the element that is close to the key
2. check if the last two element satify the requirment.

Time complexity: O(log N)
'''
def search_ceiling_of_a_number(arr, key):

    lt, rt = 0, len(arr) - 1
    while lt < rt - 1:

        mid = (lt + rt) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lt = mid + 1
        else:
            rt = mid - 1
    
    # postprocess the last two element
    if arr[lt] >= key:
        return lt
    if arr[rt] >= key:
        return rt
        
    return -1

arr = [1,3,8,10,15]
key = 12

arr = [1,3,8,15,15]
key = 15

arr = [1,3,8,10,15,15]
key = 15

rs = search_ceiling_of_a_number(arr, key)
print(rs)