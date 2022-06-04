# 字母全排列
def permutation(input, str, visited):

    # base case
    if len(str) == len(input):
        print(''.join(str))
        return

    # recursion rules
    for i in range(len(input)):
        candidate = input[i]
        if candidate in visited:
            continue

        str.append(candidate)
        visited.add(candidate)
        permutation(input, str, visited)

        # recover state
        visited.remove(candidate)
        str.pop(len(str) - 1)

# 字母组合，不允许重复字母 解法1 【a,b,c】
def all_subset(input, solution, level):
    # base case
    if level == len(input):
        print(''.join(solution))
        return
    # recursion rule
    # case 1: add input[level] into solution
    solution.append(input[level])
    all_subset(input, solution, level + 1)
    solution.pop()

    # case 2: add nothing
    all_subset(input, solution, level + 1)

# 字母组合，解法2
def all_subset_1(rs, input, solution, start):
    rs.append(list(solution))
    print(''.join(solution))
    for i in range(start, len(input)):
        solution.append(input[i])
        all_subset_1(rs, input, solution, i + 1)
        solution.pop()

# 字母组合，允许重复字母 【a,b,b,c】
def all_subset_duplicate(input, str, level):
    if level == len(input):
        print(''.join(str))
        return

    # add an element, duplicate elements would only be added if it has been added before.
    str.append(input[level])
    all_subset_duplicate(input, str, level + 1)
    str.pop()

    # skip duplicates before traversing the right branch
    i = level
    while i < len(input) and input[i] == input[level]:
        i += 1

    # add nothing
    all_subset_duplicate(input, str, i)

all_subset_duplicate(['a','b','b', 'b', 'c'], [], 0)

'''
Problem: print all combinations of coins that can sum up to a total value k
coins: list of available coins
target: target value k
index: the index of currently using coin
solution: store the number of each coin that use for a certain solution
'''
def coin_combinations(coins, target):
    solution = []
    combinations(coins, 0, solution, target)

def combinations(coins, index, solution, target):
    if index == len(coins):
        if target == 0:
            print(solution)
        return

    # i represents the number of xth coin that we pick for a certain solution
    for i in range(0, target//coins[index] + 1):
        solution.append(i)
        # go to next level, starting from next coin
        combinations(coins, index + 1, solution, target - coins[index] * i)
        solution.pop()


#coin_combinations([1, 2], 5)

# coin combination solution 2
def combination(coins, index, solution, target):

    if target == 0:
        print(solution)
        return

    if target < 0:
        return

    # i here represent ith coin in the coin list
    for i in range(index, len(coins)):
        solution.append(coins[i])
        # the next level index start from ith coin, ignoring the elements that before ith
        # so that we can avoid duplicate case such as: 1->5 and 5 -> 1
        combination(coins, i, solution, target - coins[i])
        solution.pop()

def coin_combination_1(coins, target):
    solution = []
    combination(coins, 0, solution, target)


#print()
#coin_combination_1([1, 2], 5)


'''
Problem: print all valid combination of factors that form an integer  
n: the integer
index: factors
'''
def get_factors_helper(n, index, solution):
    if n == 1:
        print(solution)
        return

    for i in range(index, n + 1):
        if n % i == 0:
            solution.append(i)
            # next level starts from i, avoiding duplicate branch.
            get_factors_helper(n // i, i, solution)
            solution.pop()

def get_factors(n):
    get_factors_helper(n, 2, [])

#get_factors(12)

'''
Time complexity: O(2^n) height of binary tree
invariant: l >= r
l: number of left parenthesis
r: number of right parenthesis
str: solution
n: total number of left or right parenthesises
'''
def valid_parenthesis(l, r, str, n):
    # base case
    if l == n and r == n:
        print(''.join(str))
        return

    # when to fill '('
    if l < n:
        str.append('(')
        valid_parenthesis(l + 1, r, str, n)
        str.pop()

    # when to fill ')'
    if l > r:
        str.append(')')
        valid_parenthesis(l, r + 1, str, n)
        str.pop()


#permutation(['a', 'b', 'c'], [], set())
#all_subset(['a','b','c'], [], 0)
#all_subset_1([], ['a','b','c','d'], [], 0)
#valid_parenthesis(0, 0, [], 3)

parent = {s: None}

def helper(s, adj):
    for v in adj[s]:
        if v not in 


def DFS(vertices, adj):

    parent = {}
    for s in vertices:
        if s not in parent:
            parent[s] = None
            helper(s, adj)
    