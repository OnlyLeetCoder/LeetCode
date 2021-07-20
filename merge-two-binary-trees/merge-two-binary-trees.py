# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def solve(root_1, root_2):
            if not root_1 and not root_2:
                return
            if not root_1:
                return root_2
            if not root_2:
                return root_1
            
            root_1.val += root_2.val
            root_1.left = solve(root_1.left, root_2.left)
            root_1.right = solve(root_1.right, root_2.right)
            return root_1
    
        return solve(root1, root2)