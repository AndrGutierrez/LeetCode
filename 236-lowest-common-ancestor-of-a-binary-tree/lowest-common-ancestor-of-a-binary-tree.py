# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
ok so we do dfs, until we find both

ok so we can do dfs, and each node and on each iteration we return, if we find both, set it

inorder, register if p or q, when we get to a root, save it as lsa untilw we find the other
"""
import math
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
                
        self.p = p.val
        self.q = q.val
        self.p_found = False
        self.q_found = False

        self.lca_level = float("inf")
        self.preOrder(root, 0)
        return self.res
    def preOrder(self, root, level):
        if root is None: return
        self.preOrder(root.left, level+1)
        if root.val == self.p or root.val == self.q:
            if root.val == self.p: self.p_found = True
            if root.val == self.q: self.q_found = True
            if level < self.lca_level:
                self.res = root
                self.lca_level = level 
        if (level < self.lca_level) and self.p_found ^ self.q_found:
            self.res = root
            self.lca_level = level

        self.preOrder(root.right, level+1)
