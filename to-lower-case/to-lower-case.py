class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        
        for i, ch in enumerate(s):
            if ch.isupper():
                s[i] = chr(ord(ch) + 32)
        
        return ''.join(s)
        