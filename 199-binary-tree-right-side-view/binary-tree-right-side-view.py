# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# its the last in the level
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        level = [root]
        res = []
        while q:
            level = list(q)
            for element in level:
                item = q.popleft()
                if item is None: continue
                if item.left: q.append(item.left)
                if item.right: q.append(item.right)
            
            if level[-1] is not None: res.append(level[-1].val)

        return res