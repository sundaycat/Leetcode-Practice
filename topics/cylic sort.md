## Problem List of slow & faster pointer ##

### **Overview**:  
循环排序(Cyclic sort或Cycle sort)。这是一种非常有用的解决这种数组：包含的数字在给定数组的长度范围内，寻找缺失或重复的数字问题的方法。

每一个元素都可以作为数组的下标(下标从0开始)。那么就可以依次遍历该数组，每次的元素和它的值对应的下标找到的元素交换，直到该下标的值和下标相等为止。这样最终可以得到一个下标值和元素相等的，排序好的数组。如果遇到大于数组长度的数，或其它不满足范围[0, length)长度的元素(负数)，直接忽略掉。

Cases that need to handle:
1. there are negative value in array
2. the values are larger than the length of the array
3. the value is not at the correct index
4. there are duplicate values in array


### Problem set 1
+ [268. Missing numbers][1]
+ [448. Find All Numbers Disappeared in an Array][2]
+ [287. Find the Duplicate Number][3]
    + [alternative slow, fast solution][4]: linkedlist loop + find the start of the loop
+ [442. Find All Duplicates in an Array][5]

### Problem set 2
+ [Find the corrupt pair][6]
+ [41. First Missing Positive][7]
+ [Find the first k missing positive][8]


[1]: https://leetcode.com/problems/missing-number
[2]: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
[3]: https://leetcode.com/problems/find-the-duplicate-number/
[4]: https://www.youtube.com/watch?v=wjYnzkAhcNk
[5]: https://leetcode.com/problems/find-all-duplicates-in-an-array/
[6]: https://www.educative.io/courses/grokking-the-coding-interview/N7Vw2GBQr6D
[7]: https://leetcode.com/problems/first-missing-positive/
[8]: https://www.educative.io/courses/grokking-the-coding-interview/g286M2Gk3YY