
'''
Given n = 4, k = 3, we have the follow recusrive tree, the time complexity is equal to the total number of nodes:
                        0
            /       /        \       \
        1           2         3       4     => C(4, 1), there is 1 size of job to achieve each combination in this level
     /  |  \      /   \       |  
    2   3   4   3       4     4             => C(4, 2), there is 2 size of job to achieve each combination in this level, Part of which is count by its upper level alreay.
  / |   |
3   4   4       4                           => C(4, 3), there is 3 size of job to achieve each combination in this level, part of which is counted by above levels already.

Time complexity: C(4, 1) + C(4, 2) + C(4, 3) <= 3C(4, 3) = O(k*C(n, k))
'''
def combine(n, k):

    res = []
    helper(res, [], 0, n, k)
    return res

def helper(res, output, start, n, k):

    # base case
    if len(output) == k:
        res.append(list(output))
        return
    
    # recursive rule
    # 用start过滤掉比当前值小的数字(因为已经便利过)
    for i in range(start + 1, n + 1):
        
        output.append(i)
        helper(res, output, i, n, k)
        output.pop()

x = combine(4, 3)
print(x)