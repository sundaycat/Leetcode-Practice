#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start

'''
Similar to leetcode 1003
'''
class Solution:
    def findComplement(self, num: int) -> int:

        if num == 0: return 1
        
        n, count = num, 0
        while n > 0:
            count += 1
            n = n >> 1
        
        allBitSet = pow(2, count) - 1
        
        return num ^ allBitSet
        
# @lc code=end

