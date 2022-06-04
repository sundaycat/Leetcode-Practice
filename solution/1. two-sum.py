def twoSum(nums, target):

    if not nums or len(nums) == 0:
        return []

    pos = {}
    for i in range(0, len(nums)):
        # use the elements in nums as key of the dictionary
        # <key: nums, value: position>
        pos[nums[i]] = i

    for j in range(0, len(nums)):
        x = target - nums[j]

        # the same element can't be used twice pos[x] != j
        if x in pos and pos[x] != j:
            return [j, pos[x]]

    return []


nums = [3, 2, 4]
x = twoSum(nums, 6)
print(x)