class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        orig = [None] * len(s)
        
        for st in s:
            string = st[:-1]
            ind = int(st[-1])
            
            orig[ind - 1] = string
        
        return ' '.join(orig)
        