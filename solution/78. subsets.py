def subsets(nums):

    res = []
    helper(res, [], 0, nums)
    return res

def helper(res, output, start, nums):
    
    res.append(list(output))
    for i in range(start, len(nums)):
        output.append(nums[i])
        helper(res, output, i + 1, nums)
        output.pop()


x = subsets([1,2,3])
print(x)