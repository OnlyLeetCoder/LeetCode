class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        marked = set()
        
        for i, ch in enumerate(s):
            if balance == 0:
                marked.add(i)
                
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                marked.add(i)
        
        ans = ''
        
        for i in range(len(s)):
            if i not in marked:
                ans += s[i]
        
        return ans
            