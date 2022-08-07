#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
from typing import List


class Solution:

    '''
    Solution 1: when the loop stops, there are 3 possible values of (lt, rt) pairs as below:

                l   r
    T x T x x x x T x x x x x T x T 
      l   r                 l   r          
    
    1. (l, r) on the far left. 
        if target < letters[lt] < letters[rt]: return lt
        if letters[lt] <= target < letterr[rt]: return rt 
    2. (l, r) in the middle of the array. 
        target <= letters[lt] < letters[rt] is always true. return rt
    3. (l, r) in the far right.
        if letters[lt] <= target < letters[rt]: return rt
        if letters[lt] <= letters[rt] <= target: return letter[0]
    '''
    def nextGreatestLetter_1(self, letters: List[str], target: str) -> str:
        
        lt, rt = 0, len(letters) - 1
        while lt < rt - 1:
            mid = (lt + rt) // 2
            # approching the target from the left.
            if letters[mid] <= target:
                lt = mid
            else:
                rt = mid

        # postprocessing the last two left elements
        if letters[lt] > target:
            return letters[lt]
        if letters[rt] > target:
            return letters[rt]
        
        return letters[0]

    '''
    Solution 2: when the loop stops, we have lt = rt + 1. so lt guarntee to be the index of the smallest element greater than target.

        r l
    x x x x x x x

    '''
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        length = len(letters)

        lt, rt = 0, len(letters) - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if letters[mid] <= target:
                lt = mid + 1
            else:
                rt = mid - 1
        
        # % for the case that the targer larger than or equal to the largest letter in array
        return letters[lt % length]

# @lc code=end

letters = ["c", "c", "f", "j"]
target = "c"

letters = ["c","f","j"]
target = "j"


# letters = ["e","e","e","e","e","e","n","n","n","n"]
# taeget = "e"

# letters = ['a', 'a', 'a']
# target = 'b'

rs = Solution().nextGreatestLetter(letters, target)
print(rs)
