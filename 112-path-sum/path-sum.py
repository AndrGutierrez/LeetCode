# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        if root:
            self.preOrder(root, 0, targetSum)
        return self.res
    def preOrder(self, node, sm, targetSum):
        if node == None:
            return None
        
        if node.left is None and node.right is None:
            if sm+node.val == targetSum:
                self.res = True

        node.left = self.preOrder(node.left, node.val+sm, targetSum)
        node.right = self.preOrder(node.right, node.val+sm, targetSum)
        return node
