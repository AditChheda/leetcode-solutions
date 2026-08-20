"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]

# Time Complexity: O(1), as we are only checking the first two edges to find the center.
# Space Complexity: O(1), as we are not using any additional data structures to store the graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list) # adjacency list
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)

        count_edges = len(d.keys()) - 1
        for key, val in d.items():
            if len(val) == count_edges:
                return key

# Time Complexity: O(E), where E is the number of edges in the graph.
# Space Complexity: O(V + E), as we are storing the graph in an adjacency list.