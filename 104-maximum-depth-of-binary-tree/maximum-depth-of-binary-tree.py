# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
ok so this is simple dfs
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, count):
        if root is None:
            self.res = max(self.res, count)
            return
        self.dfs(root.left, count + 1)
        self.dfs(root.right, count + 1)