# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(cur):
            if not cur:
                return [0,0]
            
            
            l_size ,l_coin = dfs(cur.left)
            r_size ,r_coin = dfs(cur.right)
            
            size = 1 + l_size + r_size
            coins = cur.val + l_coin + r_coin
            self.res += abs(size-coins)
            return [size,coins]
        
        dfs(root)
        return self.res
        