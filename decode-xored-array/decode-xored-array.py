class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        
        for el in encoded:
            decoded.append(decoded[-1] ^ el)
        
        return decoded