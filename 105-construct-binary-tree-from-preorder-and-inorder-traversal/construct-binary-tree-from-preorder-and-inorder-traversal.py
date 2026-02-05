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
        def build( preorder, inorder):
            nonlocal preorder_index
            if len(inorder) <= 0 or preorder_index >= len(preorder): return None

            root = TreeNode(preorder[preorder_index])
            preorder_index+=1
            i = 0

            for j, item in enumerate(inorder):
                if item == root.val:
                    i =  j
                    break

            # build left subtree
            root.left = build(preorder, inorder[:i])
            # build right subtree
            root.right = build(preorder, inorder[i+1:])

            return root 

        preorder_index = 0
        root = build(preorder, inorder)
        return root
    
