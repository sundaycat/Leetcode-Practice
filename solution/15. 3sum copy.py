from typing import List

'''
1. Sorted the array first
2. Tranform to two sum problem X + Y + Z = 0 => Y + Z = -X
3. Avoid duplicate elements using while loop and certain conditions

Time complexity: O(n^2)
Space complexity: depends on the selection of sorting algorithms
'''
class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(index, target):

            left, right = index + 1, len(nums) - 1
            while left < right:
                _sum = nums[left] + nums[right]
                if _sum < target:
                    left += 1

                if _sum > target:
                    right -= 1

                if _sum == target:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip the same elements to avoid duplicate pairs
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 
        
        
        triplets = []
        nums.sort()
        for i in range(len(nums) - 3 + 1):
            # skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            twoSum(i, -nums[i])
        
        return triplets        
        

s = Solution()
print(s.threeSum([-2, -1, 0, 2, 3]))