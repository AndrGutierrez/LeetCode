# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
left to right

is there a way to put the level backwards without reversing the array level?

doesnt seem to 
"""

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res = []

        q = deque([root])
        level_number = 0
        while q:
            level_number +=1
            level = list(q)
            if level_number % 2 == 1:
                res.append([node.val for node in level])
            else:
                res.append([node.val for node in reversed(level)])
            for _ in level:
                node = q.popleft()
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            

        return res