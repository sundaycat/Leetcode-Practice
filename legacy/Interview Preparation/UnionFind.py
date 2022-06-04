class Solution(object):

    # business number from 0 to 10
    numOfBizs = 11

    def __init__(self):
        # array record parents of each business
        self.array = [-1 for i in range(self.numOfBizs)]

    # connect biz1 and biz2(union operation)
    def markAsDuplicate(self, biz1, biz2):

        # check if biz1 and 2 are out of boundary

        # find the root of the tree that biz1, biz2 belong to
        root1 = self.findRoot(biz1)
        root2 = self.findRoot(biz2)

        # if biz1 and biz2 already connected, do nothing
        if root1 == root2:
            return

        # union by size, make smaller tree be child of larger tree
        if abs(self.array[root1]) < abs(self.array[root2]):
            # update the size of tree
            self.array[root2] += self.array[root1]
            # merge two trees
            self.array[root1] = root2
        else:
            self.array[root1] += self.array[root2]
            self.array[root2] = root1

    # check if biz1 and biz2 are connected
    def isDuplicate(self, biz1, biz2):
        # find the root of the tree that biz1, biz2 belong to
        root1 = self.findRoot(biz1)
        root2 = self.findRoot(biz2)

        # compare if biz1, biz2 share the same root
        return True if root1 == root2 else False

    # return the minimum biz(find operation)
    def resolveId(self, biz):
        # return biz itself if it's the only one item in tree
        if self.array[biz] == -1:
            return biz

        minimum = biz
        for i in range(self.numOfBizs):
            if self.isDuplicate(i, biz):
                minimum = min(i, minimum)

        return minimum

    def findRoot(self, biz):

        if self.array[biz] < 0:
            return biz

        # path compression
        self.array[biz] = self.findRoot(self.array[biz])
        return self.array[biz]


'''
        8             1
     /  |  \        / | \
    5   3   7      9  0  6  
   /
  4
  
Array: [-1, -1, -1, 8, 5, 8, -1, 8, -5, -1, -1]
         0   1   2  3  4  5   6  7   8   9  10 
'''
business = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = Solution()
# tree 1
s.markAsDuplicate(5, 4)
s.markAsDuplicate(8, 3)
s.markAsDuplicate(3, 7)
s.markAsDuplicate(5, 3)

# tree 2
s.markAsDuplicate(1, 9)
s.markAsDuplicate(1, 0)
s.markAsDuplicate(1, 6)

print(s.isDuplicate(1, 2))  # False
print(s.isDuplicate(1, 3))  # False
print(s.isDuplicate(0, 2))  # False
print(s.isDuplicate(4, 8))  # True, this also change the parent of 4 from 5 to 8

print(s.resolveId(1))  # 0
print(s.resolveId(2))  # 2
print(s.resolveId(9))  # 0



