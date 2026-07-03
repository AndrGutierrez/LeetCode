# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""we do bfs, sum each level and return the max"""
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx= -float('inf')
        i = 1
        res = i
        while q:
            curr_level = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            addition = sum(curr_level)
            if  addition > mx:
                mx = addition
                res = i
            i+=1
        return res