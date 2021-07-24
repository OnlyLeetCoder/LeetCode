class Solution:
    def squareIsWhite(self, s: str) -> bool:
        squareSum = ord(s[0]) + int(s[1])
    
        return squareSum % 2