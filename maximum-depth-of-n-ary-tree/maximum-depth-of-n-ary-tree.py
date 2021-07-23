"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxD = 0
        
        def dfs(root, d):
            if not root:
                return
            nonlocal maxD
            maxD = max(maxD, d)
            
            for child  in root.children:
                dfs(child, d+1)
            
        dfs(root, 1)
        
        return maxD