from typing import List

'''
1. 从两端向中间, 逐次比较, 选每次比较得到的较大值放入数组的尾端.
2. 循环结束条件为 left <= right循环结束条件为 left <= right

time complexity: O(N)
space complexity: O(N)
'''
class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left, right, i = 0, len(nums) - 1, len(nums) - 1
        rs = [0] * len(nums)
        while left <= right:
            
            l_square = nums[left] * nums[left]
            r_square = nums[right] * nums[right]
            if l_square >= r_square:
                rs[i] = l_square
                left += 1
            else:
                rs[i] = r_square
                right -= 1
            
            i -= 1
            
        return rs