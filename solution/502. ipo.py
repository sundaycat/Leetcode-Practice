#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
from typing import List
from heapq import *


class Solution:
    # k distinct project and w initial capitical
    # solution 1
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        minHeap, maxHeap = [], []
        for index in range(len(capital)):
            heappush(minHeap, (capital[index], index))
        
        i, maxProfit = 0, w
        while i < k:
            
            while minHeap:
                
                # if the minimum available capotal exceed the buget w, break
                if minHeap[0][0] > w or not minHeap: 
                    break

                # only when the available capital > w, we pop out the minHeap top
                avaCapital, index = heappop(minHeap)

                # push its corresponding profit to max heap
                heappush(maxHeap, -profits[index])

            # update the max profit and the available capitcal for next round
            if maxHeap:
                w += -heappop(maxHeap) 
            
            i += 1

        return w

    # soltion 2
    def find_maximum_capital(self, number_of_projects, inital_capital, profits, capital):

        max_prof_heap, min_cap_heap = [], []

        # insert all project capitals to a min heap
        for i in range(len(capital)):
            heappush(min_cap_heap, (capital[i], i))

        available_cap = inital_capital
        for i in range(number_of_projects):
            # find all projects that affortable within the available capital
            # insert them in a max heap
            while min_cap_heap and min_cap_heap[0][0] <= available_cap:
                capitial, idx = heappop(min_cap_heap)
                heappush(max_prof_heap, -profits[idx])

            # terminate if we are not able to find any project within the available capital
            if not max_prof_heap: 
                break
            
            # select the project with the maximum profit, its profit becomes the 
            # capital of next round
            available_cap += -heappop(max_prof_heap)

        return available_cap


# @lc code=end


k = 1
w = 2
capital = [1, 1, 2]
profits = [1, 2, 3]

s = Solution()
rs = s.findMaximizedCapital(k, w, profits, capital)
# rs = s.find_maximum_capital(k, w, profits, capital)
print(rs)