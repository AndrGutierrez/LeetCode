# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# values are unique
# we allow a node to be descendant of itself (see example 2)

# maybe dfs, in order?
# it can only be valid if theyre in the same tree

# traverse the tree in preOrder, if you find a p or q, save current as last common ancestor if the level is higher(smaller since we start from 0)
# if found p but not q, and you go on, save the highest level thing as latest common ancestor 
import math
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.p = p.val
        self.q = q.val
        self.pfound = False
        self.qfound = False
        self.lcalevel = math.inf
        self.preOrder(root, 0)

        return self.lca

    def preOrder(self, node, level):
        if node is None: return None

        
        self.preOrder(node.left, level + 1)
        if node.val == self.p or node.val == self.q:
            if node.val == self.p: self.pfound = True
            if node.val == self.q: self.qfound = True
            if level < self.lcalevel:
                self.lca = node
                self.lcalevel = level
        if (level < self.lcalevel) and not (self.pfound and self.qfound) and (self.pfound or self.qfound):
            self.lca = node
            self.lcalevel = level
        if self.lca: print(node.val, self.lca.val)

        self.preOrder(node.right, level + 1)
