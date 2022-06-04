from collections import defaultdict
import heapq
from typing import List
class Solution:

    def build_adjList(self, edges, succProb):
        # undirect graph
        adjList = defaultdict(list)
        for i in range(len(edges)):
            u, v, prob = edges[i][0], edges[i][1], succProb[i]
            adjList[u].append((v, prob))
            adjList[v].append((u, prob))

        return adjList
    

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adjList = self.build_adjList(edges, succProb)

        max_prob = [0 for i in range(n)]
        max_prob[start] =  1

        # probability, vertex index
        max_heap = [(-max_prob[start], start)]
        while max_heap:
            
            u_prob, u = heapq.heappop(max_heap)
            u_prob = -u_prob

            if u == end:
                return u_prob
            
            for v, uv_prob in adjList[u]:
                if max_prob[v] < u_prob * uv_prob:
                    max_prob[v] = u_prob * uv_prob
                    heapq.heappush(max_heap, (-max_prob[v], v))

        return max_prob[end]


n = 5
edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
start = 3
end = 4

s = Solution()
t = s.maxProbability(n, edges, succProb, start, end)
print(t)