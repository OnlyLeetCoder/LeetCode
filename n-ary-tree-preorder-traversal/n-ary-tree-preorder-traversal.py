"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        
        def solve(root):
            if not root:
                return
            nonlocal order
            order.append(root.val)
            
            for child in root.children:
                solve(child)
        
        solve(root)
        
        return order