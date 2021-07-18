# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        def solve(root):
            nonlocal ans
            if not root:
                return
            
            if low <= root.val <= high:
                ans += root.val
            
            if root.val > high:
                solve(root.left)
            elif root.val < low:
                solve(root.right)
            else:
                solve(root.left)
                solve(root.right)
            
        
        solve(root)
        return ans