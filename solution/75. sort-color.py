from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ''' 
        Invariant:  0: [0, lt), 1: [lt, mid), unexpored: [mid, rt], 2: (rt, ..]
            lt
        EX: [1, 0, 2, 1, 0]
            mid          rt
        '''
        lt, mid, rt = 0, 0, len(nums) - 1
        # 如果终止条件为 mid < rt, 跳出循环时, mid == rt, 其中rt从定义看仍然是一个未被探索过的元素, 需要处理.
        while mid <= rt:
            if nums[mid] == 0:
                nums[lt], nums[mid] = nums[mid], nums[lt]
                lt += 1
                mid += 1
            elif nums[mid] == 2:
                # mid doesn't change because the element at mid position remain unexplored after swapping.
                nums[mid], nums[rt] = nums[rt], nums[mid]
                rt -= 1
            else:
                mid += 1

    def sortColors_1(self, nums: List[int]) -> None:
        ''' 
        0: [0, lt), 1: [lt, mid), unexpored: [mid, rt), 2: [rt, ..)
        EX: [1, 0, 2, 1, 0]
        '''
        lt, mid, rt = 0, 0, len(nums)
        # mid == rt时, rt已经是被探索过的位置了, 因此直接结束.
        while mid < rt:
            if nums[mid] == 0:
                nums[lt], nums[mid] = nums[mid], nums[lt]
                lt += 1  # 指向下一个可被替换为0的位置
                mid += 1 # 未探索元素 + 1
            elif nums[mid] == 2:
                nums[mid], nums[rt - 1] = nums[rt - 1], nums[mid]
                rt -= 1
            else:
                mid += 1

       
            
nums = [1, 0, 2, 1, 0]
nums = [2, 0, 1]
s = Solution()
s.sortColors_1(nums)
print(nums)