
import math
from typing import List

class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # if k <= 1: return 0

        start, end, product, count = 0, 0, 1, 0
        for end in range(len(nums)):

            # Every new added elements in the window, there are new subarray combination generated and the number of them is equal to (end - start + 1). That is, combining the new elemen with every subarray of previous window.
            product *= nums[end]
            while product >= k and start < len(nums):
                product /= nums[start]
                start += 1
            
            if start <= end:
                count += end - start + 1
        
        return count


    '''
    Binary Search on Logarithms
        1. Logarithms tranfer the product problem to sum.
        2. calculate the product sum
        3. find the index most close to K via binary search for every given i to end.
    '''
    def numSubarrayProductLessThanK_BS(self, nums: List[int], k: int) -> int:

        if k == 0: return 0

        logk = math.log(k, 2)
        prefix = [0 for i in range(len(nums))]
        pre = 0
        for i in range(len(nums)):
            prefix[i] += pre + math.log(nums[i], 2)
            pre = prefix[i]

        # finding, for each i, the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k.
        ans = 0
        for i in range(len(prefix)):
            lt, rt = i, len(prefix) - 1
            temp = None
            if i - 1 < 0:
                temp = 0
            else:
                temp = prefix[i - 1]

            while lt < rt - 1:
                mid = (lt + rt) // 2

                if prefix[mid] - temp < logk - 1e-9:
                    lt = mid
                else:
                    rt = mid - 1

            index = lt if prefix[rt] - temp >= logk - 1e-9 else rt
            if nums[index] < k:
                ans += index - i + 1

        return ans


    # binary search solution optimization
    def numSubarrayProductLessThanK_BS_OPT(nums, k):

        if k == 0: return 0

        logk = math.log(k, 2)

        #数组加长1, 方便后续的计算.
        prefix = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            prefix[i + 1] += prefix[i] + math.log(nums[i], 2)

        # finding, for each i, the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k.
        ans, epsilon = 0, 1e-9
        for i in range(1, len(prefix)):
            
            # 因为整个数组时单调递增, 所以如果自穿第一个元素就大于k的话, 直接跳过.
            if nums[i - 1] >= k: continue

            lt, rt = i, len(prefix) - 1
            while lt < rt - 1:

                mid = (lt + rt) // 2

                # 减去/除去前一数值, 在得到的新的累计结果上统计符合条件的子串. 例如
                # 10, 5, 2, 6 => 0, 10, 50, 100, 600(累积)
                # round 1: i = 1, lt = 1, rt = 4 => index = 2 => (10), (10, 5)
                # round 2: i = 2, lt = 2, rt = 4 => 除以nums[1]后对应的子串: 5, 10, 60 => index = 4 => (5), (5, 2), (5, 2, 6)
                if prefix[mid] - prefix[i - 1] < logk - epsilon:
                    lt = mid
                else:
                    rt = mid - 1

            index = lt if prefix[rt] - prefix[i - 1] >= logk - epsilon else rt
            ans += index - i + 1
        
        return ans

# arr = [10, 5, 2, 6]
# k = 100

arr = [2,4,8,16,32]
k = 16

# arr = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
# k = 19

# arr = [10,3,3,7,2,9,7,4,7,2,8,6,5,1,5]
# k = 30
