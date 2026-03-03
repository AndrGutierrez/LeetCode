# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        level = list([root])
        res = []
        i = 0
        while q:
            levelsum = 0

            for item in level:
                current = q.popleft()

                if item is not None:
                    levelsum+=item.val

                    if item.left: q.append(item.left)
                    if item.right: q.append(item.right)
            n = len(level)
            if n>0:
                res.append(levelsum/n)

            level = list(q)

        return res