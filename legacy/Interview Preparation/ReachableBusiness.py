# reachable business

class Business(object):

    # nearby_biz is a hashmap where the key is nearby_biz object and value
    # is distance from the current biz to the nearby biz
    def __init__(self, name):
        self.name = name
        self.nearby_biz = {}

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


def helper(node, path_sum, dis, res, visited, distance):

    # check visited
    if node in visited:
        return

    # record visited node
    visited.add(node)

    # calculate this level path sum
    this_path_sum = path_sum + dis

    if 0 < this_path_sum <= distance:
        res.append(node.name)

    # is leaf node
    if not node.nearby_biz:
        return

    for child in node.nearby_biz:
        helper(child, this_path_sum, node.nearby_biz[child], res, visited, distance)


def main(start_node, distance):

    res = []
    visited = set()
    helper(start_node, 0, 0, res, visited, distance)
    return res


A = Business("A")
B = Business("B")
C = Business("C")
D = Business("D")

# A.nearby_biz = {B: 2, C: 4}
# B.nearby_biz = {A: 2, D: 5}
# C.nearby_biz = {A: 4}
# D.nearby_biz = {B: 5}

A.nearby_biz = {B: 2}
B.nearby_biz = {C: 3}
C.nearby_biz = {D: 4}
D.nearby_biz = {A: 5}

rs = main(A, 14)
print(rs)










