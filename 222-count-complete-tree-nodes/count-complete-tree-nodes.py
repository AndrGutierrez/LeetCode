# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
less than o(n) but not necessarily o(n), maybe o(logn)? 

maybe bfs and just count the last level

get amount of levels, then go to every except last level and count the ones that dont have complete thing, the amount will be to to the power of 0 - the amount of incomplete
"""
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if not (root.left or root.right): return 1
        current = root
        self.h = 0
        self.bottomamount= 0
        while current:
            current = current.left or current.right
            self.h+=1
        self.dfs(root, 0)
        return 2**(self.h -1) + self.bottomamount - 1 

    def dfs(self, node, level):
        if node is None or level == self.h-1: return None
        if level == self.h-2:
            if node.left: self.bottomamount +=1
            if node.right: self.bottomamount +=1
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)