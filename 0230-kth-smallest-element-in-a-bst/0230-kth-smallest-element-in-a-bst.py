# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        stack = []
        curr = root
        
        while curr or  stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            num+=1
            if num==k:
                return curr.val
            curr = curr.right
                
        
        
#         res = []
#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             res.append(root.val)
#             inorder(root.right)
            
#         inorder(root)
#         return res[k-1]
#         Iterative Solution
        
        