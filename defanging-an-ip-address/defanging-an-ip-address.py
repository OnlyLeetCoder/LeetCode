class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangIp = ''
        
        for ch in address:
            if ch == '.':
                defangIp += '[.]'
            else:
                defangIp += ch
        
        return defangIp