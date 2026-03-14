# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Traverse in preorder, check if left is smaller than root, and if right is bigger than root, revursively 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ordered = []
        self.inOrder(root)
        valid = True
        for i in range(1, len(self.ordered)):
            if self.ordered[i] <= self.ordered[i-1]:
                valid = False
        return valid
    def inOrder(self, root):
        
        if not root: return 
        self.inOrder(root.left)
        print(root.val)
        self.ordered.append(root.val)
        self.inOrder(root.right)
        