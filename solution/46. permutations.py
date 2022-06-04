# we must not visit a node twice in any "branch" of the depth-first tree 
def permute(nums):
    res = []
    visited = [False for i in range(len(nums))]
    helper(res, [], nums, visited)
    return res

def helper(res, output, nums, visited):

    if len(output) == len(nums):
        res.append(list(output))
        return
    
    for index in range(len(nums)):

        if visited[index]:
            continue
        
        # Get to the next level
        output.append(nums[index])
        visited[index] = True
        helper(res, output, nums, visited)
        visited[index] = False

        output.pop()

res = permute([1, 2, 3])
print(res)