#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
from typing import List


class Solution:

    # time complexity: O(N + M)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        rs = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):

            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            # overlapping case
            if start <= end:
                # save the overlapping area
                rs.append([start, end])

            # move forward the index of the list with smaller interval end
            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                # if the ends are the same, move both indexes forward simultaneous
                i += 1
                j += 1

        return rs  

        # end相等时, 需做多一次比较, 效率差些, 但代码更简洁.
        def intervalIntersection_2(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

            rs = []
            i, j = 0, 0
            while i < len(firstList) and j < len(secondList):

                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                
                # overlapping case
                if start <= end:
                    # save the overlapping area
                    rs.append([start, end])

                # move forward the index of the list with smaller interval end
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1

        return rs                   

firstList = [[1, 3], [5, 9]] 
secondList = []
s = Solution()
rs = s.intervalIntersection(firstList, secondList)
print(rs)

# @lc code=end

