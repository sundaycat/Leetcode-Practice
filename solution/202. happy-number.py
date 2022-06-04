class Solution:

    def isHappy(self, n: int) -> bool:

        slow, fast = n, n
        while True:

            slow = self.doSquareSum(slow)
            fast = self.doSquareSum(fast)
            fast = self.doSquareSum(fast)

            # avoid the corner case num = 1
            if fast == 1: return True
            if slow == fast:
                return False
            
    def doSquareSum(self, num):

        square_sum = 0
        while num > 0:
            
            square_sum += (num % 10)**2
            num //= 10
        
        return square_sum
    
