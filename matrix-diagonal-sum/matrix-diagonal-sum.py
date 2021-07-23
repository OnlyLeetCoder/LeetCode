class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        maxDsum = 0
        ldsum = rdsum = 0
        n = len(mat)
        
        for i in range(len(mat)):
            ldsum += mat[i][i]
            rdsum += mat[i][n-i-1]
        
        print(ldsum, rdsum)
        
        return ldsum + rdsum - (n & 1) * (mat[n//2][n//2])