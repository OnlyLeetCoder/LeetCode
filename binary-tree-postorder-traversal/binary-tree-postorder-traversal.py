# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        order = []
        
        def postorder(root):
            if not root:
                return
            
            nonlocal order
            postorder(root.left)
            postorder(root.right)
            order.append(root.val)
        
        postorder(root)
        
        return order