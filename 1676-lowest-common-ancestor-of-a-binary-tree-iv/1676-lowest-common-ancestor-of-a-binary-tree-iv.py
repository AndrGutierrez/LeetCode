# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
lowest common ancestor.

a node is a descendant of itself

values of the tree are unique

I think i already saw this and I don't exactly remember the solution

I remember this might be a dfs problem but it's a weird particular algorithm

Ok so I just checked it not gonna lie, so the thing is some kind of 

"predecessor": which is one step left and then right until you can
"successor": one step right and left till you can


number of nodes is in the order of 10^4 so it has to be O(n)

well if we find a "predecessor" we can...

so the thing is it's an ancestor of both... yeah we cannot use bfs

ok also it isn't just the LCA of two nodes, its the LCA of multiple nodes

I mean I think we can do dfs, inorder and have levels passed, so the level

Ok so the brute force approach is doing dfs on each node and seeing if we can find them all...

but thats O(n^2)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        targets = set(nodes)
        def dfs(n):
            if n is None or n in targets:
                return n
            L = dfs(n.left)
            R = dfs(n.right)
            if L and R:
                return n
            return L or R
        return dfs(root)