# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        order = []
        
        def solve(root):
            if not root:
                return
            nonlocal order
            solve(root.left)
            order.append(root.val)
            solve(root.right)
        
        solve(root)
        
        return order