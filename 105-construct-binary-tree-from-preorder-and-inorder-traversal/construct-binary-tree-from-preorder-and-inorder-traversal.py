# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
reconstruct tree based in preorder and inorder
returns a node

perorder and inorder is size of 3*10**3, so kind of a medium size

pere order and in order have UNIQUE values

both are guaranteed to be a solution
pre
n   l  r   l   r
[3, 9, 20, 15, 7]
in
l   n  r   n   r
[9, 3, 15, 20, 7]

go in this order, left, root, right, if any is filled go to next

pre[i].left = in[i] if in[i]!=pre[i] else: None,
in[i].left = pre[i+1] if pre[i+1] !=in[i] else: None


buildSubtree

root pre order
todos hasta encontrar root en inorder son el subarbol izquierdo
todos despues de ese son el subarbol derecho

si len(inorder) = 1
return nodo

si no

pasa al siguiente en pre order
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        added={}
        root = self.build(preorder, inorder, added)
        return root
    def build(self, preorder, inorder, added):
        # build left subtree

        if len(inorder) <= 0 or len(preorder)<=0: return None
        # print(added.get(preorder[0]))
        while added.get(preorder[0]):
            preorder = preorder[1:]
            if len(preorder) <=0: return None

        added.setdefault(preorder[0], True)

        root = TreeNode(preorder[0])

        if inorder[0] == root: return root

        i = 0
        for j, item in enumerate(inorder):
            if item == root.val:
                i =  j
                break

        # build left subtree
        uno =1

        root.left = self.build(preorder[uno:], inorder[:i], added)

        if root.left!=None: uno+=1
        # build right subtree
        root.right = self.build(preorder[uno:], inorder[i+1:], added)

        # base case
        return root 