# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode(-1)
        tail = head
        
        def inorder(root):
            nonlocal tail
            
            if not root:
                return
            inorder(root.left)
            tail.right = TreeNode(root.val)
            tail = tail.right
            inorder(root.right)
        
        inorder(root)
        
        return head.right