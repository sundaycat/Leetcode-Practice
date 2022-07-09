## Problem List of DFS ##

DFS = Recursive + Guessing. Linked the solution space to graph. Figure out the following 
 1. what is the nodes(节点).
 2. what is the base case and recursive rules.
 3. what is the breaches? when to backtrack or go further(分支, 方向).
 4. what is the invariant of each level? when to restock the states

### problem set 1
+ [17. Combination of phone numbers][1]
+ [22. Generate paretheses][2]
+ [46. Permutations][3] - state space
+ [77. Combinations][4]
+ [78. Subsets][5]

### problem set 2
+ [51. N queens][6]
+ [37. Sudoku solver][7]: reference: [graph coloring][17]
+ [36. Valid Sudoku][8]

### probelm set 3

Different conditions where to start and stop searching. somtimes we need visited array to track the cells we visited before.

+ [200. Number of islands][9]
+ [695. Max area of Island][16]
+ [1020. Number of enclaves][10]
+ [130. Surrounded regions][11]
+ [79. Word search][12]
    + follow up: could you use search pruning to make your solution faster with a larger(DP记录每一个cell的位置和对应的word index)
+ [302. Smallest rectangle enclosing black pixels][13]

### problem set 4

Groking the interview pattern problem list

+ [112. Path Sum][20]
+ [113. Path Sum II][21]
+ [129. Sum Root to Leaf Numbers][22]
+ [1430. path with given sequence][24]
+ [437. Path Sum III][25]
+ [543. Diameter of Binary Tree][26]
+ [124. Binary Tree Maximum Path Sum][23] (Need more practice)
---

## Reference
1. [Permutation][14]
2. [Leetcode problems set][15]
3. [Kenny talks code][18]
4. [smallest rectangle black pixels solution][19]

---

[1]: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
[2]: https://leetcode.com/problems/generate-parentheses/
[3]: https://leetcode.com/problems/permutations/
[4]: https://leetcode.com/problems/combinations/
[5]: https://leetcode.com/problems/subsets/
[6]: https://leetcode.com/problems/n-queens/
[7]: https://leetcode.com/problems/sudoku-solver/
[8]: https://leetcode.com/problems/valid-sudoku
[9]: https://leetcode.com/problems/number-of-islands
[10]:https://leetcode.com/problems/number-of-enclaves
[11]:https://leetcode.com/problems/surrounded-regions
[12]:https://leetcode.com/problems/word-search
[13]:https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels
[14]:http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
[15]:https://medium.com/@koheiarai94/60-leetcode-questions-to-prepare-for-coding-interview-8abbb6af589e
[16]:https://leetcode.com/problems/max-area-of-island/
[17]:[https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072]
[18]: https://www.reddit.com/r/csMajors/comments/pu9tyk/kenny_talks_code_list_of_leetcode_problems/
[19]: [https://xiaoguan.gitbooks.io/leetcode/content/LeetCode/302-smallest-rectangle-enclosing-black-pixels-hard.html]
[20]: https://leetcode.com/problems/path-sum/
[21]: https://leetcode.com/problems/path-sum-ii/
[22]: https://leetcode.com/problems/sum-root-to-leaf-numbers/
[23]: https://leetcode.com/problems/binary-tree-maximum-path-sum/
[24]: https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/
[25]: https://leetcode.com/problems/path-sum-iii/
[26]: https://leetcode.com/problems/diameter-of-binary-tree/
[27]: https://leetcode.com/problems/binary-tree-maximum-path-sum/