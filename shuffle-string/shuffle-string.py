class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffStr = [None] * len(s)
        
        for i, ch in enumerate(s):
            shuffStr[indices[i]] = s[i]
        
        return ''.join(shuffStr)