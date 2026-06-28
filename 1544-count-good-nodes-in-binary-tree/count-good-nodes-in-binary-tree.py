# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

"""
ok so we have to do a dfs passing a maxvalue, if we meet the cirteria sum 1 to the response
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, -float('inf'))
        return self.res
    def dfs(self, root, maxVal):
        if root is None:
            return
        if not maxVal > root.val:
            self.res+=1

            maxVal = root.val
        self.dfs(root.left, maxVal)
        self.dfs(root.right, maxVal)
        