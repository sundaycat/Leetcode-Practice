# https://www.youtube.com/watch?v=5eIK3zUdYmE
# Bellman-ford

from collections import defaultdict
import heapq


def build_adjList(flights):

    # (departure, destination, price)
    adjList = defaultdict(list)
    for depart, dest, price in flights:
        adjList[depart].append((dest, price))
    return adjList

# Dijkstra
def findCheapestPrice(flights, src, dst, stops):

    # By dijkstra
    adjList = build_adjList(flights)

    # cost, stop level, airport index 
    min_heap = [(0, 0, src)]
    while min_heap:

        cost, level, u = heapq.heappop(min_heap)
        # the first path we met from src to dst is guarnteed to be the shortest one within in k stops
        if u == dst:
            return cost
        
        # start from level 0 and the number of stops is always one less than the level(number of total nodes in path)
        if level < stops + 1:
            for v, w_uv in adjList[u]:
                heapq.heappush(min_heap, (cost + w_uv, level + 1, v))

    return -1

# Bellman-ford
def findCheapestPrice_1(n, flights, src, dst, stops):

    prices = [float('inf') for i in range(n)]
    prices[src] = 0

    for i in range(stops + 1):
        # temp use for updates
        # price use to store each round's original statue before edge relaxtion
        temp = prices.copy()
        for u, v, cost in flights:
            # temp might got update mutiple time during each round, so we need to reflect it.
            if temp[v] > prices[u] + cost:
                temp[v] = prices[u] + cost
        prices = temp

    return prices[dst] if prices[dst] != float('inf') else -1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

print(findCheapestPrice(flights, src, dst, k))
print(findCheapestPrice_1(n, flights, src, dst, k))