class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxAmt = 0
        
        for row in accounts:
            maxAmt = max(maxAmt, sum(row))
            
        return maxAmt