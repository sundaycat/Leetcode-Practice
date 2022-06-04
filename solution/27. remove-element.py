from typing import List


class Solution:

    '''
    i: always point to the next element that can be replaced
    j: iterate through the array
    satisfy: [0, i), unsatisfy: [i, j), unexplore: [j, )
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            
            j += 1
        
        return i