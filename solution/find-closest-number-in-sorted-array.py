'''
In this problem, we need to keep the middle element for the next iteration, so to avoid the dead loop, we change the stop condition to lt < rt -1 and postprocessing the last two elements later.
'''
def find_cloest_num(nums, target):
    
    # keep the midd for next, change end condition to left + 1 < right
    lt, rt = 0, len(nums) - 1
    while lt < rt - 1:

        mid = (lt + rt) // 2
        if nums[mid] < target:
            lt = mid 
        elif nums[mid] > target:
            rt = mid
        else:
            return mid

    # post-processiong the last two elements
    ans = lt if abs(nums[lt] - target) <= abs(nums[rt] - target) else rt
    return ans

nums = [1,2,5,9]
target = 3
rs = find_cloest_num(nums, target)
print('index: {}, num: {}'.format(rs, nums[rs]))

