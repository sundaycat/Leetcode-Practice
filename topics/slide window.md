## Problem List of Slide window ##
### **Overview**:   
Usually involves the realionship of subarray and main array and require the time complexity to be O(n) and space complexity to be O(1)

+ **Key points**:
    + construct windows(fix size, flexible size)
    + the condition to shrink and move to next window

+ **Trick**:
    + Using dictionary to track the frequency elements fall inside the window
    + Using while loop to shrink the windows

### Problem set 1
+ [643. Maximum Average Subarray I][1] - fix window size
+ [209. Minimum Size Subarray Sum][2] - flexible window size
+ [340. Longest Substring with At Most K Distinct Characters][3] - using hashmap
+ [904. Fruit Into Baskets][4] 
+ [003. Longest Substring Without Repeating Characters][5]
+ [424. Longest Repeating Character Replacement][6] - max count
    + [1004. Max Consecutive Ones III][7] - follow up question of 424

### Problem set 2
+ [567. Permutation in String][8] - hashmap, pattern count, match count
    + [438. Find All Anagrams in a String][9]
+ [076. Minimum Window Substring][10]
+ [030. Substring with Concatenation of All Words][11]


### Reference

[1]: https://leetcode.com/problems/maximum-average-subarray-i
[2]: https://leetcode.com/problems/minimum-size-subarray-sum
[3]: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
[4]: https://leetcode.com/problems/fruit-into-baskets
[5]: https://leetcode.com/problems/longest-substring-without-repeating-characters
[6]: https://leetcode.com/problems/longest-repeating-character-replacement
[7]: https://leetcode.com/problems/max-consecutive-ones-iii
[8]: https://leetcode.com/problems/permutation-in-string
[9]: https://leetcode.com/problems/find-all-anagrams-in-a-string
[10]: https://leetcode.com/problems/minimum-window-substring
[11]: https://leetcode.com/problems/substring-with-concatenation-of-all-words