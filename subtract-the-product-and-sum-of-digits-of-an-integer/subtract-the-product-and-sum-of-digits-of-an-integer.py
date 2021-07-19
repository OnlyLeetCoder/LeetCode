class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        def digitByDigit(n):
            dprod = 1
            dsum = 0
            
            while n:
                rem = n % 10
                dprod *= rem
                dsum += rem
                
                n //= 10
            
            return dprod, dsum
        
        prod, sum = digitByDigit(n)
        
        return prod - sum