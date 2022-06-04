'''
The question is equavilent to find the longest substring with no more than 2 distinct characters

Input: fruits = [1,2,3,2,2]
Output: 4
'''
from typing import List


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:

        start, end, max_val, bucket = 0, 0, 0, {}
        for end in range(len(fruits)):

            fruit = fruits[end]
            if fruit not in bucket:
                bucket[fruit] = 0
            bucket[fruit] += 1
            
            # shrink the window until its length <= 2
            while len(bucket) > 2:

                in_bucket = fruits[start]
                bucket[in_bucket] -= 1
                if bucket[in_bucket] == 0:
                    del bucket[in_bucket]
                
                start += 1
            
            # compare the max length with the length of the current window
            max_val = max(max_val, end - start + 1)
        
        return max_val