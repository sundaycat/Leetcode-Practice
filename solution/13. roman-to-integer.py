def roman_to_int(s):

    if not s or len(s) == 0:
        return 0

    roman_nums = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000, IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
    i, rs = 0, 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_nums:
            rs += roman_nums[s[i:i+2]]
            i += 2
        else:
            rs += roman_nums[s[i]]
            i += 1

    return rs


test = "LVIII"
print(roman_to_int(test))

print(len(test))
print(min([1,2,3]))