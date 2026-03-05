# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        level = [root]
        while q:
            level_size = len(q)
            level_values = []
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    level_values.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(level_values) > 0: res.append(level_values)
            

        return res
