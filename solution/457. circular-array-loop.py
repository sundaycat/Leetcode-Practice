from typing import List

'''
1. The cycle should have more than one element. This means that when we move a pointer forward, if the pointer points to the same element after the move, we have a one-element cycle.

2. The other requirement mentioned in the problem is that the cycle should not contain both forward and backward movements. 

Follow up: In our algorithm, we don't keep a record of all the numbers that have been evaluated for cycles. We know that all such numbers will not produce a cycle for any other instance as well. If we can remember all the numbers that have been visited, our algorithm will improve to O(N) as, then, each number will be evaluated for cycles only once. We can keep track of this by creating a separate array, however, in this case, the space complexity of our algorithm will increase to O(N).

Cycle detection in a directed graph(each node only has one child)

'''
class Solution:

    def circularArrayLoop(self, nums: List[int]) -> bool:

        def move_foward(direction, cur, next):

            # different direction
            if (nums[next] >= 0) != direction:
                return False

            # only one element in circle
            if cur == next:
                return False
            
            return True

        # searching for cycle for each element
        for start in range(len(nums)):

            # remembering the direction of each element while searching for the cycle
            direction = (nums[start] >= 0)

            slow = fast = start
            while True:

                cur = fast
                fast = (fast + nums[fast]) % len(nums)
                if not move_foward(direction, cur, fast):
                    break
            
                cur = fast
                fast = (fast + nums[fast]) % len(nums)
                if not move_foward(direction, cur, fast):
                    break
                
                slow = (slow + nums[slow]) % len(nums)
                if slow == fast:
                    return True
            
        return False

nums = [3, 1, 4]
s = Solution()
x = s.circularArrayLoop(nums)
print(x)