class Solution:
    def findComplement(self, num: int) -> int:
        bdig = 0
        temp = num
        
        while temp:
            bdig += 1
            temp >>= 1
        
        return (1 << bdig) - num - 1