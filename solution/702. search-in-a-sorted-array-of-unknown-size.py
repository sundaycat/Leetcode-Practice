import math

class ArrayReader(object):

	def __init__(self, arr):
		self.arr = arr
	
	def get(self, index):
		if index >= len(self.arr):
			return math.inf
		return self.arr[index]

'''
Solution:
1. find the proper bounds of the array that contains the target. A efficient way to find the bounds is to start at the beginning of the array with the bound's size as 1 and exponentially increase the bound's size (i.e., double it) until we find the bounds that can have the key. O(log N)
2. apply binary search to find the index of the target. O(log N)

Time complexity: O(log N) where N is maximum length of the array.
'''
def search_in_infinite_array(reader, key):

	# find the proper bound that contains the key
	lt, rt = 0, 1
	while reader.get(rt) < key:
		newLt = rt + 1
		rt += (rt - lt + 1) * 2
		lt = newLt
	
	# find the key index via binary search in searchable bounds
	while lt <= rt:
		mid = lt + (rt - lt) // 2
		if reader.get(mid) == key:
			return mid
		elif reader.get(mid) < key:
			lt = mid + 1
		else:
			rt = mid - 1
	
	return -1


def main():
	reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
	print(search_in_infinite_array(reader, 16))
	print(search_in_infinite_array(reader, 11))
	reader = ArrayReader([1, 3, 8, 10, 15])
	print(search_in_infinite_array(reader, 15))
	print(search_in_infinite_array(reader, 200))

main()