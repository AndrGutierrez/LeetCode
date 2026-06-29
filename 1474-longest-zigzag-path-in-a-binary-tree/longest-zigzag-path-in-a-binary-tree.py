# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
longest zigzag is dfs, ok so we can pass a iszigzag or smth like that
"""
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.dfs(root, None, 0)
        return self.max
    def dfs(self, root, last, count):
        if root is None:
            return
        
        self.max = max(self.max, count)
        if last == "right":
            self.dfs(root.left, "left", count+1)
        else:
            self.dfs(root.left, "left", 1)
        if last == "left":
            self.dfs(root.right, "right", count+1)
        else:
            self.dfs(root.right, "right", 1)

        return