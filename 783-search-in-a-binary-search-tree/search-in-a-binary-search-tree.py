# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

"""
ok so find the value and return the node found
"""
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.target = val
        self.res = None
        self.search(root)
        return self.res

    def search(self, root):
        if not root or self.res: return
        if root.val == self.target: self.res = root
        if root.left:
            if root.val > self.target:
                self.search(root.left)
        if root.right:
            if root.val < self.target:
                self.search(root.right)