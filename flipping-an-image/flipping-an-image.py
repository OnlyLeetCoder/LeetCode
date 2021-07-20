class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        for i in range(n):
            for j in range(m//2):
                image[i][j],image[i][m-j-1]  = image[i][m-j-1], image[i][j]
            
            for j in range(m):
                image[i][j] ^= 1
        
        return image