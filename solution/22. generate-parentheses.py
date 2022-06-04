def generateParenthesis(n):
        
    res = []
    helper(res, [], 0, 0, n)
    return res
        
def helper(res, valid_str, left, right, n):

    # base case
    if len(valid_str) == n*2:
        res.append(''.join(valid_str))
        return
    
    # rescurive rule
    if left < n: #左括号不能大于括号总数
        valid_str.append('(')
        helper(res, valid_str, left + 1, right, n)
        valid_str.pop()

    if right < left: # 左括号数要大于右括号数,表示总有一个左括号先于未被添加的右括号出现, 此时可以添加右括号
        valid_str.append(')')
        helper(res, valid_str, left, right + 1, n)
        valid_str.pop()
        

# optimize 1
def generateParenthesis(n):
        
    res = []
    helper(res, '', 0, 0, n)
    return res
        
def helper(res, valid_str, left, right, n):

    # base case
    if len(valid_str) == n*2:
        res.append(valid_str)
        return
    
    # rescurive rule
    if left < n:
        helper(res, valid_str+'(', left + 1, right, n)

    if right < left:
        helper(res, valid_str+')', left, right + 1, n)


# Optimaize 2
def generateParenthesis(n):
    
    res = []
    def helper(valid_str, left, right, n):
        # base case
        if len(valid_str) == n*2:
            res.append(valid_str)
            return

        # rescurive rule
        if left < n:
            helper(valid_str+'(', left + 1, right, n)

        if right < left:
            helper(valid_str+')', left, right + 1, n)             
    
    helper('', 0, 0, n)
    
    return res