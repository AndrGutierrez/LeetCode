# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
the biggest problem I had with this was thinking about these arrays in a recursive way and figuring out I have to handle duplicats

then came optimization
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        root = self.build(preorder, inorder)

        return root
    def build(self, preorder, inorder):

        if len(inorder) <= 0 or len(preorder)<=0: return None


        root = TreeNode(preorder[-1])

        if inorder[0] == root: return root

        i = 0
        for j, item in enumerate(inorder):
            if item == root.val:
                i =  j
                break

        preorder.pop()

        # build left subtree
        root.left = self.build(preorder, inorder[:i])
        # build right subtree
        root.right = self.build(preorder, inorder[i+1:])

        return root 