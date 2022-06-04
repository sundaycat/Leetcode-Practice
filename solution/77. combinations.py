def combine(n, k):

    res = []
    helper(res, [], 1, n, k)
    return res

def helper(res, output, start, n, k):

    # base case
    if len(output) == k:
        res.append(list(output))
        return
    
    # recursive rule
    # 用start过滤掉比当前值小的数字(因为已经便利过)
    for i in range(start, n + 1):
        
        output.append(i)
        helper(res, output, i + 1, n, k)
        output.pop()

x = combine(4, 2)
print(x)