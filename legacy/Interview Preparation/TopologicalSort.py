class NTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.children = []

# topologically sort the graph, DFS
def topSort(adjList):

    visited = set()
    stack = []
    for vertex in adjList:

        if vertex in visited:
            continue

        visited.add(vertex)
        topSortHelper(adjList, vertex, stack, visited)

    return stack[-1]

def topSortHelper(adjList, vertex, stack, visited):

    if vertex not in adjList:
        stack.append(vertex)
        return

    for child in adjList[vertex]:

        if child in visited:
            continue

        visited.add(child)
        topSortHelper(adjList, child, stack, visited)

    stack.append(vertex)

# Build the tree from root, DFS
def buildTree(rootVal, adjList):
    root = NTreeNode(rootVal)
    for child in adjList[root.value]:
        childNode = NTreeNode(child)
        root.children.append(childNode)
        buildTreeHelper(childNode, adjList)

    return root

def buildTreeHelper(node, adjList):

    if node.value not in adjList:
        return

    for child in adjList[node.value]:
        childNode = NTreeNode(child)
        node.children.append(childNode)
        buildTreeHelper(childNode, adjList)

def CompanyArchitecture(relations):

    # transform the relations to a adjacent list using dictionary
    adjList = {}
    for relation in relations:

        if relation[0] not in adjList:
            adjList[relation[0]] = [relation[1]]
        else:
            adjList[relation[0]].append(relation[1])

    # topologically sorts the graph and find the root
    rootVal = topSort(adjList)

    # build the tree
    root = buildTree(rootVal, adjList)
    return root


x = [["Ben", "Charles"], ["Ben", "Denis"], ["Henry", "Cook"], ["Alice", "Ben"], ["Alice", "Henry"], ["Alice", "Peter"]]
source = CompanyArchitecture(x)

# print the tree, BFS
cur = []
cur.append(source)
while cur:
    next = []
    for item in cur:
        print(item.value, end=", ")
        next = next + item.children

    print()
    cur = next