class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 2
        deg = [0] * n
        
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
        
        for i in range(n):
            if deg[i] == n-2:
                return i