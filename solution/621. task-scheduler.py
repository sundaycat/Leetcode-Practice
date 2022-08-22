#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter, deque
from typing import List
from heapq import *


class Solution:

    '''
    Solution 1: 
    1. In each iteration, we try to execute as many as n+1 tasks. 
    2. For the next iteration, we put all the waiting tasks back in the Max Heap. 
    3. If, for any iteration, we are not able to execute n+1 tasks, the CPU has to remain idle for the remaining time in the next iteration.
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:

        dict = {}
        for task in tasks:
            if task not in dict:
                dict[task] = 0
            dict[task] += 1

        maxHeap = []
        for task, freq in dict.items():
            heappush(maxHeap, (-freq, task))
        
        count, queue = 0, deque()
        # res = []
        while maxHeap:
           
            # try to execute as many as n + 1 task from maxHeap
            i = 0
            while maxHeap and i < n + 1:
                
                count += 1

                freq, task = heappop(maxHeap)
                # res.append(task)
                freq += 1
                if -freq > 0:
                    queue.append((freq, task))
            
                i += 1
            
            # push all the task in queue back to heap
            while queue:
                freq, task = queue.popleft()
                heappush(maxHeap, (freq, task))
            
            # we'll be having 'n' idle intervals before the next iteration
            if maxHeap:
                count += (n + 1) - i
                # res.extend(['' for i in range(n - i + 1)])

        return count

    
    # Soluiton 2: https://wwww.youtube.com/watch?v=s8p8ukTyA2I
    # set up an time ticker to monitor the process
    # keep the restore time for each task we push into the queue.
    def leastInterval_2(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:

            time += 1
            if maxHeap:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heappush(maxHeap, queue.popleft()[0])
        
        return time


        
# @lc code=end

# output = 7
tasks = ['a', 'a', 'a', 'b', 'c', 'c']
n = 2
print(Solution().leastInterval(tasks, n))