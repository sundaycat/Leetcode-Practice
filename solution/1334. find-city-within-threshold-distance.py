from collections import defaultdict
import heapq
from typing import List
from collections import defaultdict

# 把每个点当成起点, 跑一遍dijstra算法
class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adjList = self.build_adjList(edges)
        
        min_len = float('inf')
        max_src = float('-inf')
        for src in range(n):

            neighbor_count = 0
            visited = set ()

            weights = [float('inf') for i in range(n)]
            min_heap = [(0, src)]
            while min_heap:

                du, u = heapq.heappop(min_heap)
                if u in visited:
                    continue
                visited.add(u)

                # neighbors doesn't include src itself, and also revisited point doesn't count
                if u != src and du <= distanceThreshold:                
                    neighbor_count += 1

                for v, w_uv in adjList[u]:
                    if weights[v] > du + w_uv:
                        weights[v] = du + w_uv
                        heapq.heappush(min_heap, (weights[v], v))
        
            if neighbor_count <= min_len:
                min_len = neighbor_count
                max_src = max(src, max_src)
        
        return max_src

    def build_adjList(self, edges):

        adjList = defaultdict(list)
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        return adjList


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

s = Solution()
x = s.findTheCity(n, edges, distanceThreshold)
print(x)
