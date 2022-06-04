# O(n^2), in place
def insertion_sort_1(arr):
    for j in range(1, len(arr), 1):
        i = j - 1
        while i >= 0 and arr[i + 1] < arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i = i - 1

def insert_sort(arr):
    
    if not arr or len(arr) == 1:
        return arr
    
    for i in range(1,len(arr)):

        num = arr[i]
        for j in range(i, -1, -1):

            if j <= 0 or num > arr[j-1]:
                arr[j] = num
                break

            arr[j] = arr[j-1]
    return arr



temp = [8, 2, 4, 9, 3, 6]
insert_sort(temp)
print(temp)