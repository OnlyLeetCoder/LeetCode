# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level_sum = defaultdict(lambda: 0)
        level_node_cnt = defaultdict(lambda: 0)
        
        def dfs(root, ht):
            if not root:
                return
            
            level_node_cnt[ht] += 1
            level_sum[ht] += root.val
            dfs(root.left, ht+1)
            dfs(root.right, ht+1)
        
        dfs(root, 0)
        
        ans = []
        
        for l in level_node_cnt:
            ans.append(level_sum[l]/level_node_cnt[l])
        
        return ans