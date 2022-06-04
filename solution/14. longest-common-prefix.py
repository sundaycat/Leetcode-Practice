# solution 1
def longest_common_prefix(strs):

    if not strs or len(strs) == 0:
        return ""

    # find the string have minimum length in the list
    min_len = min([len(str) for str in strs])

    # pre_len use to store the length of common string
    pre_len = -1
    for i in range(0, min_len):
        cm_char = strs[0][i]
        # is_common use to indicate whether or not the current char is common
        is_common = True
        for str in strs:
            if str[i] != cm_char:
                is_common = False
                break

        if is_common:
            pre_len = i
        else:
            break

    rs = "" if pre_len == -1 else strs[0][:pre_len+1]
    return rs

# solution 2: divide and conquer O(S), S = m*n
def longest_common_prefix_2(strs):
    return helper(strs, 0, len(strs)-1)    
  
def find_common(str1, str2):

    min_len = min(len(str1), len(str2))

    i = 0
    for i in range(0, min_len):
        if str1[i] != str2[i]:
            break
    
    return str1[0:i]
    
def helper(strs, left, right):

    if right - left + 1 == 1:
        return strs[left]
            
    mid = (left + right) // 2
    lt_com = helper(strs, left, mid)
    rt_com = helper(strs, mid+1, right)
        
    return find_common(lt_com, rt_com)


# solution 3: binary search O(Slogm), S=m*n
def is_common_prefix(strs, start, end):
        
        s = strs[0][start:end+1]
        i = 1
        while i < len(strs):
            if s != strs[i][start:end+1]:
                break
            i += 1
        
        if i < len(strs):
            return False
        
        return True
    
def longest_common_prefix_3(strs):
   
    min_len = min([len(s) for s in strs])
    low, high = 0, min_len - 1
    while low <= high:
        
        mid = (low + high) // 2
        if is_common_prefix(strs, low, mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return strs[0][0:low]

# reference: 
#   https://www.geeksforgeeks.org/longest-common-prefix-using-divide-and-conquer-algorithm/
#   https://www.geeksforgeeks.org/longest-common-prefix-using-binary-search/
test = ["flower", "flow", "flight"]
print(longest_common_prefix_3(test))