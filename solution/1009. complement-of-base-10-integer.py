#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start

'''
Given number: 101, its one's complement(反码) is 010. Then

    number ^ one's complement = 101 ^ 010 = 111 = all bits set. 

Let us add 'number' on both side, we have

    number^number^one's complement = number^all bits set = 101^101^010 = 010 = one's complement

That is, one's complement = number ^ all bits set.

Solution:
1. find the number of binary bit that need to represent a number
2. generate the all set bits with the given binary bit
3. calcuate its complement by number xor all bits set
'''
class Solution:

    def bitwiseComplement(self, n: int) -> int:

        # corner case
        if n == 0:
            return 1

        # 1. find the number of binary bit to represent the number
        num, count = n, 0
        while num > 0:
            count += 1
            num = num >> 1
        
        # 2. generate all set bits. Ex: pow(2, 2) - 1 = 100 - 001 = 11 
        allSetBits = pow(2, count) - 1
        
        # 3. calcuate the one's complement of the given number
        return n ^ allSetBits
        
# @lc code=end

# 1000 = 8
print(pow(2, 0)) 


print(Solution().bitwiseComplement(0))