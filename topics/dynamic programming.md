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

---
#### Useful subproblems for strings / sequences x

- Suffixes x[i:]
- Prefixes x[:i]
- Substrings[i : j]

Time Complexity: 
1. suffixes, prefixes $O(|X|)$
2. substring $O(|X|^2)$

---
#### two kind of guessing
1. guess which other subproblems to use
2. add subproblems & constrains to "remember state"
2. subproblem expension, often with extra constrains that let us remember some states about the past
---
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

#### problem list 1: one dimension
+ [70. Climb Stairs][2]
+ [322. Coin Changes][3] 
+ [300. Longest Increasing Subsequence][4]
+ [139. Word Break][5]

#### problem list 2: two dimension
+ [1143. Longest Common Subsequence][6] (suffix, prefix)
+ [10. Regular Expression Match][7] (suffix, prefix)
+ [5. Longest Palindromic Substring][8] (substring)

#### problems list: with constrains


#### problem list 4
+ [329. Longest Increasing Path in a Matrix][9]

### reference
[DP View of Bellman-Ford Algorithm][1]


---
[1]: https://www.youtube.com/watch?v=OQ5jsbhAv_M&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=19
[2]: https://leetcode.com/problems/climbing-stairs
[3]: https://leetcode.com/problems/coin-change
[4]: https://leetcode.com/problems/longest-increasing-subsequence
[5]: https://leetcode.com/problems/word-break
[6]: https://leetcode.com/problems/longest-common-subsequence
[7]: https://leetcode.com/problems/regular-expression-matching
[8]: https://leetcode.com/problems/longest-palindromic-substring
[9]: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/