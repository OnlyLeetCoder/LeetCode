class Solution:
    def countBits(self, n: int) -> List[int]:
        bitArr = []
        
        def getSetBits(n):
            ans = 0
            while n:
                if n & 1:
                    ans += 1
                n >>= 1
            return ans
        
        for i in range(n+1):
            bitArr.append(getSetBits(i))
        
        return bitArr