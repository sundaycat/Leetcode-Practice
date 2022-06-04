# brute force, dynamic programing O(n^2)
def max_area(height):

    max_area = 0
    for j in range(1, len(height)):
        for i in range(j-1, -1, -1):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
        
    return max_area

'''
If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.
'''
# two pointer O(n), greedy algorithm
def max_area_1(height):

    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        '''
        elif height[left] > height[right]:
            right -= 1
        else: #height[left] == height[right]:
            left += 1
            right -= 1
        '''
    return max_area

# 48762645
print(max_area_1([4,3,2,1,4]))
print(max_area_1([1,8,6,2,5,4,8,3,7]))

print(max_area_1([5,4,1,15,2,5]))
print(max_area_1([5,4,1,15,2,5]))