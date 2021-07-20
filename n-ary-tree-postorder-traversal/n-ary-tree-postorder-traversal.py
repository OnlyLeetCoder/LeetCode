"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []
        
        def solve(root):
            if not root:
                return
            nonlocal order
            
            for child in root.children:
                solve(child)
            
            order.append(root.val)
        
        solve(root)
        
        return order