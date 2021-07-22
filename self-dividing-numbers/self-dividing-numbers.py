class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDiv(n):
            x = n
            while x:
                r = x % 10
                if not r or n % r:
                    return False
                x //= 10
            return True
        
        selfDivs = []
        
        for i in range(left, right+1):
            if isSelfDiv(i):
                selfDivs.append(i)
        
        return selfDivs