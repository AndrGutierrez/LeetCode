# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

"""
ok so this looks like dfs

but how do we get the amount of paths

like we could store the sum of each path we take

we pass the sum on each call.... no because vals can also be negative

we can save  sum at each point, but then if we try to calculate the sum without a thing

well we can do dfs from each node and then try to find... yeah, its gonna be something like O(n²) but the input size allows for that i think
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.target = targetSum
        self.simpleDfs(root)
        return self.res
    def dfs(self, root, acc):
        if root is None:
            return

        if acc + root.val == self.target:
            self.res +=1

        self.dfs(root.left, acc + root.val)
        self.dfs(root.right, acc + root.val)

    def simpleDfs(self, root):
        if root is None:
            return
        if root.val == self.target:
            self.res+=1

        self.dfs(root.left, root.val)
        self.dfs(root.right, root.val)

        self.simpleDfs(root.left)
        self.simpleDfs(root.right)