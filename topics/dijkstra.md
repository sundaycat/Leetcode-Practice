## Problem List of DFS ##

Dijkstra is an algorithm that use to find the shortest path in a graph.
1. check the proof on the algorithm note. 
2. note that the vertex that pop out of the min_heap, its weight can not be relax any more.
3. build adjacent list, keep track of visited notes, relax the edges that going out of the current vertex.

### problem set
+ [743. Network Delay Time][1]
+ [787. Cheapest Flights with K stops][2]
+ [1514.Path with Maximum Probability][3]
+ [1334.Find the city with the Smallest Number of Neighbors at a Threshold Distance][4]
+ [1631.Path with Minimum Effort][5]
+ [77. Combinations][4]
+ [78. Subsets][5]


### Reference
1. [Leetcode problem list][6]
2. [Shortest path, Dijkstra's Algorithm][7]
3. [Why Dijkstra doesn't work with negative weights][8]

[1]: https://leetcode.com/problems/network-delay-time/
[2]: https://leetcode.com/problems/cheapest-flights-within-k-stops/
[3]: https://leetcode.com/problems/path-with-maximum-probability/
[4]: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
[5]: https://leetcode.com/problems/path-with-minimum-effort/
[6]: https://leetcode.com/list/?selectedList=92iyptd5
[7]: https://www.youtube.com/watch?v=xhG2DyCX3uA
[8]: https://stackoverflow.com/questions/13159337/why-doesnt-dijkstras-algorithm-work-for-negative-weight-edges