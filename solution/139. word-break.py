from typing import List

'''
1. subproblem: dp(i): does exist a subseqence starting from i till i + len(word) that maches any words in the dict. X[i:]
2. guess: any word in the dict
3. relate subproblems: dp(i) = dp(i + len(word)) 

reference: https://www.youtube.com/watch?v=Sx9NNgInc3A
'''
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        rs = self.helper(0, s, wordDict, memo)
        print()
    
    def helper(self, i, s, wordDict, memo):
        
        if i == len(s):
            return True

        if i in memo:
            return memo[i]
        
        ans = False
        for word in wordDict:

            if word != s[i : i + len(word)]:
                continue
            
            # 只要有一个分支为真, 则返回真
            ans = self.helper(i + len(word), s, wordDict, memo)
            if ans:
                break

        memo[i] = ans
        return ans


    # bottom up algorithm
    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:

        memo = [False for i in range(len(s) + 1)]
        memo[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                
                # skip if the index go beyond the boundary or no word in dict matches
                offset = len(word)
                if i + offset > len(s) or s[i : i + offset] != word:
                    continue

                # DP rules: 当前转态已经和字典中的某一单词匹配了, 如果当前单词的下一个单词对应的状态也匹配的话, 则当前状态为真.  
                memo[i] = memo[i + offset]

                # 只要任意一个分支为真, 则该状态为真, 跳出
                if memo[i]:
                    break

        return memo[0]

x = Solution()
# s = 'cars'
# wordDict = ['car', 'ca', 'rs']
s = "abcd"
wordDict = ["a","abc","b","cd"]
print(x.wordBreakBottomUp(s, wordDict))