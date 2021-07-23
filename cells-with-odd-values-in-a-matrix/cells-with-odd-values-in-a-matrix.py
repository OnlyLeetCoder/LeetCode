class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0 for i in range(n)] for j in range(m)]
        
        for r, c in indices:
            for i in range(m):
                mat[i][c] += 1
            
            for j in range(n):
                mat[r][j] += 1
        
        return sum(mat[i][j] % 2 for j in range(n) for i in range(m))