class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while True:
            if not x and not y:
                break
            bx = x & 1
            by = y & 1
            
            if bx != by:
                ans += 1
                
            x >>= 1
            y >>= 1
        
        return ans