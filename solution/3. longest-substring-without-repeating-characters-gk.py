# solution 1 brute force O(n^3)
# Check all the possible substrings, using a set to check if the substring contains duplicate letters
def is_unique(s, start, end):

    letters = set()
    for i in range(start, end):
        if s[i] in letters:
            return False
        letters.add(s[i])

    return True

def length_of_longest_substr_1(s):

    n = len(s)
    max_len = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if is_unique(s, i, j):
                max_len = max(max_len, j - i)

    return max_len

# solution 2 O(n) Sliding Window
'''
A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the 
array/string which usually defined by the start and end indices, i.e. [i,j) (left-closed, right-open). A sliding window 
is a window "slides" its two boundaries to the certain direction. For example, if we slide [i,j) to the right by 1 elem
-ent, then it becomes [i+1,j+1) (left-closed, right-open).
'''
def length_of_longest_substr_2(s):

    char_freq = {}
    max_len = 0
    slow = 0
    for fast, char in enumerate(s):
        # get(): if the char doesn't exist in the dict, assign value of 0 to it, otherwise increase its freq by 1
        char_freq[char] = char_freq.get(char, 0) + 1

        # move the slow pointer to the next un-duplicate position(移到出现重复的字符的下一位)
        while char_freq[char] > 1:
            # while moving, decrease the freq by 1 for all the chars that slow visited
            char_freq[s[slow]] -= 1
            slow += 1

        # update the max_len, note that fast is included
        max_len = max(max_len, fast - slow + 1)

    return max_len

# follow-ups:
# 1. return the substring
def follow_up_1(s):

    char_freq = {}
    slow = 0
    max_len = 0
    start, end = 0, 0
    for fast, char in enumerate(s):
        # get(): if the char doesn't exist in the dict, assign value of 0 to it, otherwise increase its freq by 1
        char_freq[char] = char_freq.get(char, 0) + 1

        # move the slow pointer to the next un-duplicate position(移到出现重复的字符的下一位)
        while char_freq[char] > 1:
            # while moving, all the freq of chars that slow pointer visited should be decreased by 1 since they are new
            # to the new substring
            char_freq[s[slow]] -= 1
            slow += 1

        # update max_len, start and end index, note fast is included
        if max_len < fast - slow + 1:
            max_len = max(max_len, fast - slow + 1)
            start, end = slow, fast

    return s[start:end + 1]

# 2. find the substring with at most k occurrence of the same type of letter
# " while char_freq[char] > k:"
def follow_up_2(s, k):

    char_freq = {}
    max_len = 0
    slow = 0
    for fast, char in enumerate(s):
        # get(): if the char doesn't exist in the dict, assign value of 0 to it, otherwise increase its freq by 1
        char_freq[char] = char_freq.get(char, 0) + 1

        # move the slow pointer to the next un-duplicate position(移到出现重复的字符的下一位)
        while char_freq[char] > k:
            # while moving, decrease the freq by 1 for all the chars that slow visited
            char_freq[s[slow]] -= 1
            slow += 1

        # update the max_len, note that fast is included
        max_len = max(max_len, fast - slow + 1)

    return max_len

# 3. return the last longest substring that satisfy the requirement
# "f max_len <= fast - slow + 1"
def follow_up_1(s):

    char_freq = {}
    slow = 0
    max_len = 0
    start, end = 0, 0
    for fast, char in enumerate(s):
        # get(): if the char doesn't exist in the dict, assign value of 0 to it, otherwise increase its freq by 1
        char_freq[char] = char_freq.get(char, 0) + 1

        # move the slow pointer to the next un-duplicate position(移到出现重复的字符的下一位)
        while char_freq[char] > 1:
            # while moving, all the freq of chars that slow pointer visited should be decreased by 1 since they are new
            # to the new substring
            char_freq[s[slow]] -= 1
            slow += 1

        # update max_len, start and end index, note fast is included
        if max_len <= fast - slow + 1:
            max_len = max(max_len, fast - slow + 1)
            start, end = slow, fast

    return s[start:end + 1]


test = "BDEFGADE"
print(follow_up_1(test))