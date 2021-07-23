from math import inf

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = maxAlt = 0
        
        for el in gain:
            alt += el
            maxAlt = max(maxAlt, alt)
        
        return maxAlt