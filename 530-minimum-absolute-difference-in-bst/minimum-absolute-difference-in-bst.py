# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# go to left 
#
#
#
#

import math
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nums = []

        self.inOrder(root)
        diffs = []
        for i in range(1, len(self.nums)):
            diff = self.nums[i] - self.nums[i-1]
            diffs.append(diff)
        return min(diffs)        
    def inOrder(self, root):
        if root is None:
            return None
        
        self.inOrder(root.left)
        self.nums.append(root.val)
        self.inOrder(root.right)

        