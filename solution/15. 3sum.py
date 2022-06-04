def two_sum(arr, start, target, triplets):
    
    # start stores the current index of outerloop element
    left, right = start + 1, len(arr) - 1
    while left < right:
        pair_sum = arr[left] + arr[right]
        if pair_sum < target:
            left += 1
        
        if pair_sum > target:
            right -= 1
        
        if pair_sum == target:
            triplets.append([arr[start], arr[left], arr[right]])
            left += 1
            right -= 1

            # skip the same element to avoid duplicate pairs
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1


def search_triplets(arr):

    triplets = []
    arr.sort()
    for i in range(len(arr) - 3 + 1):
        # skip the same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        two_sum(arr, i, -arr[i], triplets)

    return triplets

test = [-1,0,1,2,-1,-4]
test = [0,0,0,0]
print(search_triplets(test))