'''
Input: [1, 3, 8, 4, 3], key=4 	=> 	Output: 3

1. Find the index of the peak of the array
2. Now, we break the array into two sub-array. One is sorted in ascending order, the order is sorted in decending order.
3. Apply binary search algorithm to the two sub-arrays.
'''
def search_bitonic_array(arr, key):

	peak = findPeak(arr)
	keyIdx = binarySearch(arr, key, 0, peak)
	if keyIdx == -1:
		keyIdx = binarySearch(arr, key, peak + 1, len(arr) - 1)
	
	return keyIdx

def findPeak(arr):

	lt, rt = 0, len(arr) - 1
	while lt < rt - 1:

		mid = (lt + rt) // 2
		if arr[mid - 1] < arr[mid] > arr[mid + 1]:
			return mid
		elif arr[mid] < arr[mid - 1]:
			lt = mid + 1
		else:
			rt = mid - 1
	
	return lt if arr[lt] > arr[rt] else rt


def binarySearch(arr, key, lt, rt):

    # decide sorted order of the current array
	direction = arr[lt] < arr[rt]
	while lt <= rt:
		mid = (lt + rt) // 2
		if arr[mid] == key:
			return mid
		elif arr[mid] < key:
			if direction:
				# increasing
				lt = mid + 1
			else:
				# decreasing
				rt = mid - 1
		else:
			if direction:
				rt = mid - 1
			else:
				lt = mid + 1
	
	return -1 


print(search_bitonic_array([1, 3, 8, 4, 3], 4))
print(search_bitonic_array([3, 8, 3, 1], 8))
print(search_bitonic_array([1, 3, 8, 12], 12))
print(search_bitonic_array([10, 9, 8], 10))