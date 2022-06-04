from typing import List

class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def threeSum(start):

            for j in range(start + 1, len(nums)):

                if j > start + 1 and nums[j] == nums[j - 1]:
                    continue
                
                lt, rt = j + 1, len(nums) - 1
                while lt < rt:

                    _sum = nums[start] + nums[j] + nums[lt] + nums[rt]    
                    if _sum > target:
                        rt -= 1
                    
                    if _sum < target:
                        lt += 1
                    
                    if _sum == target:

                        rs.append([nums[start], nums[j], nums[lt], nums[rt]])
                        lt += 1
                        rt -= 1

                        while lt < rt and nums[lt] == nums[lt - 1]:
                            lt += 1
                        while lt < rt and nums[rt] == nums[rt + 1]:
                            rt -= 1  

        nums.sort()
        rs = []
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            threeSum(i)
            
        return rs    

nums = [1,0,-1,0,-2,2]
target = 0

s = Solution()
print(s.fourSum(nums, target))

# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
