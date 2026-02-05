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
        def build(left, right):
            nonlocal preorder_index
            if left > right: return None
            val = preorder[preorder_index]
            root = TreeNode(val)
            preorder_index+=1



            # build left subtree
            root.left = build(left, inorder_index_map[val]-1)
            # build right subtree
            root.right = build(inorder_index_map[val]+1, right)

            return root 

        preorder_index = 0
        inorder_index_map = {
            num: i for i, num in enumerate(inorder)
        }
        root = build(0, len(preorder)-1)
        return root
    
