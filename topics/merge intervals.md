## Problem List of merge intervals ##

### **Overview**:   

This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if the overlap.

Given two intervals('a' and 'b'), there will be six different ways the two intervals can relate to each other:

1. 'a' and 'b' do not overlap
2. 'a' anb 'b' overlap, 'b' ends after 'a'
3. 'a' completely overlaps 'b'
4. 'a' & 'b' overlap, 'a' ends after 'b'
5. 'b' completely overlaps 'a'
6. 'a' and 'b' do not overlap

Understanding the above six cases will help us in solving all intervals related problems.
+ we usually need to sort the intervals.
+ overlapping condition: 
    ``` python
    start = min(intervals[left][start], intervals[right][start])
    end = min(intervals[right][end], intervals[right][end])
    if start > end: 
        overlapping
    ```
### Problem set 1
+ [56. merge intervals][1]
+ [57. insert interval][2]
+ [986. interval list intersections][3]
+ [435. non-overlapping intervals][4] - greedy + interval scheduling
    + Sort and iterate through the intervals. If there is overlapping found, alway keep the interval with the earilest end time as it produces the maximal capacity to hold rest intervals. That is, the overlapping interval with a larger end time might overlapping with the ones come after it.

### Problem set 2
+ [253. meeting rooms II][5]
+ [maximum CPU load][6]
+ [759. employee free time][7]
    + solution: merge sort + min heap; [sweepline algorithm][11]
    + [lincode 850][10]
### Reference
[non-overlapping interval 1][8]
[non-overlapping interval 2][9]


[1]: https://leetcode.com/problems/merge-intervals
[2]: https://leetcode.com/problems/insert-interval
[3]: https://leetcode.com/problems/interval-list-intersections
[4]: https://leetcode.com/problems/non-overlapping-intervals
[5]: https://leetcode.com/problems/meeting-rooms-ii
[6]: https://www.educative.io/courses/grokking-the-coding-interview/xVlyyv3rR93
[7]: https://leetcode.com/problems/employee-free-time/
[8]: https://www.youtube.com/watch?v=BTObFnHbD4U
[9]: https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling
[10]: https://www.lintcode.com/problem/850/
[11]: https://en.wikipedia.org/wiki/Sweep_line_algorithm