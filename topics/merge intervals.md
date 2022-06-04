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

Understanding the above six cases will help us in solving all intervals related problems. We usually need to sort the intervals before sloving the problem.

### Problem set 1
+ [56. merge intervals][1]
+ [57. insert interval][2]
+ [986. interval list intersections][3]

### Problem set 2



[1]: https://leetcode.com/problems/merge-intervals
[2]: https://leetcode.com/problems/insert-interval
[3]: https://leetcode.com/problems/interval-list-intersections