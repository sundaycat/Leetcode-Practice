# we must not visit a node twice in any "branch" of the depth-first tree 
'''
time complexity: O(n!) if copy list doesn't count, else O(n*n!)
space complexity: O(n)
'''
def permute(nums):

    res = []
    visited = [False for i in range(len(nums))]
    helper(res, [], nums, visited)
    return res

def helper(res, output, nums, visited):

    if len(output) == len(nums):
        # have to copy the original list since we resuse it during recusing.
        res.append(list(output))
        return
    
    for index in range(len(nums)):

        if visited[index]:
            continue
        
        # prepare the state change for the next level
        output.append(nums[index])
        visited[index] = True

        # get to the next level
        helper(res, output, nums, visited)

        # restore the state of current level when return from next level 
        visited[index] = False
        output.pop()

res = permute([1, 2, 3])
print(res)