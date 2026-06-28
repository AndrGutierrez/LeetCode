# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
have an array for each one, 
do bfs, when reaching a leaf append, we have to do it inorder or preorder, anything but posorder i think
check if they're the same"""
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        arr1 = self.dfs(root1, [])
        arr2 = self.dfs(root2, [])

        return arr1 == arr2
    def dfs(self, root, arr):
        if not root: return arr
        if not root.left and not root.right:
            arr.append(root.val)
            return arr
        arr = self.dfs(root.left, arr)
        arr = self.dfs(root.right, arr)
        return arr