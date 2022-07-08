'''
letter combination
'''
def letter_combination(digits):

    res = []
    if digits is None or len(digits) == 0:
        return res
    
    # represent 2 - 9 keyboard letters
    dict = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    helper(digits, 0, dict, [], res)
    return res
    
def helper(digits, index, dict, comb_str, res):

    # base case
    if index == len(digits):
        res.append(''.join(comb_str))
        return

    # recursive rule
    letters = dict[int(digits[index])]
    for letter in letters:
        comb_str.append(letter) 
        helper(digits, index + 1, dict, comb_str, res)
        comb_str.pop()


x = letter_combination('234')
print(x)