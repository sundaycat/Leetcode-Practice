from typing import List


class Solution:

    # 区间划分为: satisfy: [0 : i], unsatisfy: (i, j), unexplored: [j : )
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i, j = 0, 0
        while j < len(nums):

            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            
            j += 1
        
        return i + 1

    
    # 遵循的左闭右开原则, satisfy: [0 : i), unsatisfy: [i, j), unexplored: [j : )
    def removeDuplicates2(self, nums: List[int]) -> int:

        i, j = 1, 1
        while j < len(nums):

            if nums[i - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            
            j += 1
        
        return i