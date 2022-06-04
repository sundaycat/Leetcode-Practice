# n: num of nodes
# times: (ui, vi, wi)
# k: start nodes
from collections import defaultdict
import heapq

def network_delay_time(times, n, k):

    adjList = build_adjList(times)

    weights = [float('inf') for i in range(n+1)]
    weights[k] = 0

    #return Dijkstra(adjList, weights, k)
    return Dijkstra2(adjList, n, k)

def build_adjList(times):
    '''
    The functionality of both dictionaries and defualtdict are almost same except for the fact 
    that defualtdict never raises a KeyError. It provides a default value for the key that does 
    not exists
    '''
    adjList = defaultdict(list)
    for u, v, w in times:
        adjList[u].append((v, w))
    return adjList

def Dijkstra(adjList, weights, k):

    visited = set()
    max_time = 0

    # (0, k) <=> (current shorest path weight, node index)
    min_heap = [(0, k)]
    while min_heap:

        du, u = heapq.heappop(min_heap)

        # if u is already in S, then du = δ(s,u), weight of shortest path from s to u
        if u in visited:
            continue

        visited.add(u)
        max_time = max(max_time, du)

        for v, w_uv in adjList[u]:
            if weights[v] > du + w_uv:
                weights[v] = du + w_uv
                heapq.heappush(min_heap, (weights[v], v))
    
    return max_time if len(visited) == len(weights) - 1 else -1


def Dijkstra2(adjList, n, k):

    visited = set()
    max_time = 0

    # (0, k) <=> (current shorest path weight, node index)
    min_heap = [(0, k)]
    while min_heap:

        du, u = heapq.heappop(min_heap)

        # if u is already in S, then du = δ(s,u), weight of shortest path from s to u
        if u in visited:
            continue
        visited.add(u)
        
        max_time = max(max_time, du)

        for v, w_uv in adjList[u]:
            heapq.heappush(min_heap, (du + w_uv, v))
    
    return max_time if len(visited) == n else -1

    
# times = [[1, 2, 10], [1,3,3],[2,3,1],[3,2,4],[2,4,2],[3,4,8],[4,5,9],[5,4,7],[3,5,2]]

# times = [[2,1,1],[2,3,1],[3,4,1]]
# times = [[1, 2, 1]]
times = [[1,2,1],[2,3,2],[1,3,4]]
n = 3
k = 1
x = network_delay_time(times, n, k)
print(x)