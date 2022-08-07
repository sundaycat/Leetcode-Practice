## Binary Search

### **Overview**

Binary search search in a sorted sequence for a target. It partition the sequence to two halves by `mid` and determine the answer in one of the halves. Each iteration reduces the search range by half. 

##### key point

- To prevent integer overflow, change `mid = (lt + rt) // 2` to `mid = lt + (rt - lt) // 2`. This [post][7] covers this bug.
- There are 3 base case, sometimes we can combine some of them according to the requirments
    ``` 
    if mid < target: lt = mid / mid + 1
    if mid > target: rt = mid / mid - 1
    if mid = target: found
    ```
- Stop condition
    + If the middle element is not considered in next iteration `lt/rt = mid +/- 1`, then we use `lt <= rt`
    + If the middle element is considered in the next iteration `lt/rt = mid`, then we use `lt < rt - 1` as our stop condition. 
        + This is to jump out the the dead loop for last two element. For example, [1 ,2, 5], target = 3.
        + Postprocessing the last two elements as we jump out of loop without comparing them. 

---

### problem set 1
+ Find Target Number in Sorted Array - `lt <= rt`
+ [074. Search a 2D Matrix][3]
+ Find Closest Number in Sorted Array - `lt < rt - 1`, consider mid for next round.
+ Find first/last occurence of target number in sorted array - combine base cases
    + [034. Find First and Last Position of Element in Sorted Array][5]
    + [658. Find K Closest Elements][4]
+ [162. Find Peak Element][6] - The array is not necessary to be sorted to apply `BS`.
+ [033. Search in Rotated Sorted Array][1]


### problem set 2
+ [Search Ceiling Number][15]
    + [Search Floor Number][16]
    + [035. Search Insert Position][8]
+ [744. Find Smallest Letter Greater Than Target][9]
+ [034. Find First and Last Position of Element in Sorted Array][5]
+ [702. Search in a Sorted Array of Unknown Size][10]
+ [Bitonic Array Maximum][13]
+ [Search Bitonic Array][11]
+ [033. Search in Rotated Sorted Array][1] - no duplicates
+ [081. Search in Rotated Sorted Array II][12] - with duplicates
+ [Rotation Count][14]
    + [153. Find Minimum in Rotated Sorted Array][17] - no duplicate
    + [154. Find Minimum in Rotated Sorted Array II][18] - with duplicates

### problem set 3


[1]: https://leetcode.com/problems/search-in-rotated-sorted-array/
[2]: https://leetcode.com/problems/kth-missing-positive-number
[3]: https://leetcode.com/problems/search-a-2d-matrix/
[4]: https://leetcode.com/problems/find-k-closest-elements/
[5]: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
[6]: https://leetcode.com/problems/find-peak-element/
[7]: https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
[8]: https://leetcode.com/problems/search-insert-position/
[9]: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
[10]: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
[11]: https://www.educative.io/courses/grokking-the-coding-interview/7n3BlOvqW0r
[12]: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
[13]: https://www.educative.io/courses/grokking-the-coding-interview/RMyRR6wZoYK
[14]: https://www.educative.io/courses/grokking-the-coding-interview/7nPmB8mZ6vj
[15]: https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7
[16]: https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7#Similar-Problems
[17]: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
[18]: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/