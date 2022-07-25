# Dynamic Programming

D.P. is a powerful algorithmic design technique. 

<pre>
D.P. = careful brute force 
     = recursion + guessing + memoization 
     = DFS + memoization
     = shortest paths in some DAG
</pre>

* Memoize: remember and reuse solutions to subproblems that help solve the problem
* DP only applies to the problems that have optimial structure and its subproblem dependencies should be acyclic otherwise we have a dead loop.
    - Optimal structure: An optimal solution to a problem contains optimal solution to subproblem
    - Overlapping subproblems: A recursive solution contains a "small" number of distinct subproblems repeated many times

---

#### Five steps to build up a D.P. Solution

1. define subproblems
2. guess
3. relate subproblem solutions
4. build dynamic programming
    - 4.1 recurse + memoize, check subproblems acyclic
    - 4.2 build D.P. table bottom-up, draw topological order first
5. solve original problem

time complexity = O(#subproblems x O(time))

#### Useful subproblems for strings / sequences x

- Suffixes x[i:]
- Prefixes x[:i]
- Substrings[i:j]

Time Complexity: 
1. suffixes, prefixes $O(|X|)$
2. substring $O(|X|^2)$

#### Two kind of guessing
1. guess which other subproblems to use to solve bigger problems
2. guess which other subproblems to use to solve bigger problems with constrains (knapack)
    + we will create subproblems with constrains. that is, the expression of subproblems often comes with constrains that let us remember some states about the past.

>In detail, remember with the knapsack problem, we had a sequence of items, each of which has value and size. We have a target knapsack with some limited capacity. We want to pack as many valuable items into the knapsack as possible. And the apparent subproblems for this problem are suffixes of the items. But suffix isn't quite enough because we don't know how much of the capacity we used up in the prefix that we have skipped over. So we have to remember the capacity we used up in the prefix.

>We did that by multiplying every subproblem by "S" different choices, which is how many units of the knapsack remain. So in some sense, we remember more about the prefix. We can also think of it in a more forward direction; we have a suffix subproblem, and we have to solve it at S different times, considering all of the different versions of this subproblem, like what if I had a 0 size, smaller or larger knapsack respectively. In some sense, we are solving more sub-problems. From a guessing perspective, we remember more information about the past.


#### Code Template
1. Naive algorithm
``` python

# Naive algorithm
def fib_1(n):

    if n <= 2:
        f = 1
    else:
        f = fib(n - 1) + fib(n - 2)
    
    return f
```

2. Top down algorithm
``` python
memo = {}
def fib_2(n):

    if n in memo:
        return memo[n]

    if n <= 2:
        f = 1
    else:
        f = fib_2(n - 1) + fib_2(n - 2)

    memo[n] = f
    return f
```

3. Bottom up D.P algorithm
``` python
def fib_3(n):

    memo = {}
    for i in range(n):
        
        if i <= 2:
            f = 1
        else:
            f = memo[i - 1] + memo[i - 2]

        f = memo[i]
    return memo[n]
```

---

#### Problem list 1: mit 6.006
+ **Basic idea of DP**
    + Fibonacci number
    + Shortest Paths (bellman ford)
+ **Five steps of sovling DP**
    + [68. Text Justification][13] 
    + Perfect Information Blackjack
+ **How to deal with sequence of DP problem**
    + [Parenthesization][16] (Matrix chain multiplication)
        + [1039. Minimum Score Triangulation of Polygon][14]
        + [312. Burst Balloons][15]
    + edit distance (&LCS)
    + Knapsack (suffice with constrians, DP function have to reflect the constrains)
        + [474. Ones and Zeroes][18]
        + [416. Partition Equal Subset Sum][17]
        + [518. Coin change 2][20]
        + [more problems][19]
+ **Two kind of gussesing**
    + Piano/Guitar fingering
    + Tetris training
    + super mario brothers.

#### Problem list 2: one dimension
+ [70. Climb Stairs][2]
+ [322. Coin Changes][3] 
+ [300. Longest Increasing Subsequence][4]
+ [139. Word Break][5]

#### Problem list 3: two dimension
+ [1143. Longest Common Subsequence][6] (suffix, prefix)
+ [10. Regular Expression Match][7] (suffix, prefix)
+ [5. Longest Palindromic Substring][8] (substring)
+ [329. Longest Increasing Path in a Matrix][9]

#### Problems list 4: with constrains
+ [714. Best Time to Buy and Sell Stock with Transaction Fee][10]
+ [416. Partition Equal Subset Sum][11] (0-1 Knapsack)
+ [337. House Robber III][12]

---

# Reference
+ [DP View of Bellman-Ford Algorithm][1]


[1]: https://www.youtube.com/watch?v=OQ5jsbhAv_M&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=19
[2]: https://leetcode.com/problems/climbing-stairs
[3]: https://leetcode.com/problems/coin-change
[4]: https://leetcode.com/problems/longest-increasing-subsequence
[5]: https://leetcode.com/problems/word-break
[6]: https://leetcode.com/problems/longest-common-subsequence
[7]: https://leetcode.com/problems/regular-expression-matching
[8]: https://leetcode.com/problems/longest-palindromic-substring
[9]: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
[10]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
[11]: https://leetcode.com/problems/partition-equal-subset-sum/
[12]: https://leetcode.com/problems/house-robber-iii/
[13]: https://leetcode.com/problems/text-justification/
[14]: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
[15]: https://leetcode.com/problems/burst-balloons/
[16]: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/1515627/problem-pattern-matrix-chain-multiplication
[17]: https://leetcode.com/problems/partition-equal-subset-sum/
[18]: https://leetcode.com/problems/ones-and-zeroes/
[19]: https://leetcode.com/discuss/study-guide/1200320/Thief-with-a-knapsack-a-series-of-crimes
[20]: https://leetcode.com/problems/coin-change-2/