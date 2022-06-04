'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
def int_to_roman(num):

    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i, res = 0, ''
    while i < len(nums):
        res += (num // nums[i]) * numerals[i]
        num %= nums[i]
        i += 1
    return res