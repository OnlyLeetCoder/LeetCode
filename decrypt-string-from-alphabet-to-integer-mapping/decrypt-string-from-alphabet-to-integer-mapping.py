class Solution:
    def freqAlphabets(self, s: str) -> str:
        destr = ''
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                asci = int(s[i]+s[i+1])
                destr += chr(ord('a')+asci-1)
                i += 3
            else:
                destr += chr(ord('a')+int(s[i])-1)
                i += 1
        
        return destr