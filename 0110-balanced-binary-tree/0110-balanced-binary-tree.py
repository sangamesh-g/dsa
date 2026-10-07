# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            if left==-1:
                return -1

            if right==-1:
                return -1

            bal=abs(left-right)
            return -1 if bal>1 else 1+max(left,right)
        
        return True if dfs(root)!=-1 else False