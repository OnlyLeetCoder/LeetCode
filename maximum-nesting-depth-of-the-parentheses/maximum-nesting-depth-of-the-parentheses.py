class Solution:
    def maxDepth(self, s: str) -> int:
        stack = [0]
        maxD = 0
        
        for ch in s:
            if ch == '(':
                stack.append(stack[-1] + 1)
            elif ch == ')':
                d = stack.pop()
                maxD = max(maxD, d)
        
        return maxD