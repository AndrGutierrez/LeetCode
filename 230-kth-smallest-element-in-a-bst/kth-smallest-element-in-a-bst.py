# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
its a BST
we can get sorted by traversing in order,

convert into an array that will be a sorted array

put number of iterations and return when the iteration is k
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.inOrder(root)
        return self.arr[k-1]

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)
