from typing import List

'''
Leetcode expects us to use greedy algorithm algoritm. Here I am using the dynamic programming
to solove the problem. The final result is a bit different from the one given by greedy.

reference: 
1. https://www.youtube.com/watch?v=RORuwHiblPc&t=302s
2. https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/TextJustification.java

solution:
1. memoized DP algorithm
2. buttom up DP algorithm
'''

class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        length = [len(word) for word in words]
        cost = [float('inf') for i in range(len(words)+1)]
        parent = [-1 for i in range(len(words) + 1)]

        for i in range(len(words), -1, -1):
            self.DP(words, maxWidth, cost, length, parent, i)

        return parent

    def DP(self, words, max_width, cost, length, parent, i):
        
        if i == len(words):
            return 0

        if cost[i] != float('inf'):
            return cost[i]

        for j in range(i + 1, len(words) + 1):

            total_width = sum(length[i:j]) + (j - i - 1)
            if total_width < max_width:
                badness = (max_width - total_width)**2
            else:
                badness = float('inf')

            cost[j] = self.DP(words, max_width, cost, length, parent, j)
            if cost[i] > badness + cost[j]:
                cost[i] = badness + cost[j]
                parent[i] = j
            
        return cost[i]


    def interpret(self, parent, words):
        
        start = 0
        while start < len(words):
            
            end = parent[start]
            text = " ".join(words[start:end])
            print(text)
            
            start = parent[start]


words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
words = ["Tushar", "Roy", "likes", "to", "code"]
maxWidth = 10

s = Solution()
parent = s.fullJustify(words, maxWidth)
print(parent)
s.interpret(parent, words)
