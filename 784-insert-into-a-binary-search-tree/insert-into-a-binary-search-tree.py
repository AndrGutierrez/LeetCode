# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
i think we can make array and then convert to bst blud
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        self.val = val
        self.search(root)
        return root
    def search(self, root):
        if not root: return

        if root.val > self.val:
            if not root.left: root.left = TreeNode(self.val)
            else:
                self.search(root.left)
        if root.val < self.val:
            if not root.right:
                root.right = TreeNode(self.val)
            else:
                self.search(root.right)
        