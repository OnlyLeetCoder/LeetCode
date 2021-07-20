class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = ans = 0
        
        for ch in s:
            if ch == 'L':
                balance -= 1
            else: balance += 1
            
            if balance == 0:
                ans += 1
        
        return ans