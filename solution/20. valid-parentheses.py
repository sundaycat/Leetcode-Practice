def is_valid(s):

    if not s or len(s) == 0:
        return True

    brackets = {'}': '{', ')': '(', ']': '['}
    stack = []
    for char in s:
        if stack and char in brackets and brackets[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return False

    return True

test = "([)]"
print(is_valid(test))


