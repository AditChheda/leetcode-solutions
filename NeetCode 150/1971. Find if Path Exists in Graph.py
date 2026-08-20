"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = {source} # set

        d = defaultdict(list) # adjacency list
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
        
        def dfs_recursive(node):
            if node == destination:
                return True
            for neighbor in d[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs_recursive(neighbor):
                        return True
            return False
        
        return dfs_recursive(source)

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space Complexity: O(V + E), as we are storing the graph in an adjacency list and also using a set to 
# keep track of seen vertices.