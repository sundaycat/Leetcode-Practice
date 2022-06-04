class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        idx1 = len(s) - 1
        idx2 = len(t) - 1

        while idx1 >= 0 or idx2 >= 0:

            idx1 = self.getNextChar(s, idx1)
            idx2 = self.getNextChar(t, idx2)
            
            # if s and t are equal after applying backspace, they should reach the end of the string simultaneously.
            if idx1 < 0 and idx2 < 0:
                return True
            
            # if either of them reach the end before the other, then they are not equal.
            if idx1 < 0 or idx2 < 0:
                return False
            
            # s and t are not equal if the next char are not the same
            if s[idx1] != t[idx2]:
                return False
            
            idx1 -= 1
            idx2 -= 1
        
        return True
    

    def getNextChar(self, str, idx):

        backspace = 0
        while idx >= 0:

            if str[idx] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                break

            idx -= 1

        return idx



str1 = "ab##"
str2 = "c#d#"
s = Solution()
print(s.backspaceCompare(str1, str2))