# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
looks like dfs

same as last but save everything in self and add

"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        self.dfs(root, '')
        return self.res
    def dfs(self, node, path):
        if node is None: return
        if node.left is None and node.right == None:
            self.res += int(f"{path}{node.val}")

        self.left = self.dfs(node.left, f"{path}{node.val}")
        self.right = self.dfs(node.right, f"{path}{node.val}")
