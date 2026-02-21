# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
nodes where each pair of adjacent has an edge connecting them

sequence does not need to pass through the root!

path sum is the sum of all nodes in path

a node can only appear in the sequence at most once

maximum sum of not empty path

bfs or dfs maybe both?


i think dfs

check all the possible path combinations?

that might just be too much

doing it while traversing the tree...

biggest pathsum of subtree
"""

# from collections import deque
# import math
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res = self.dfs(root)
#         return res
#     
#     def dfs(self, node):
#         if node is None: return -math.inf
#         if node.left is None and node.right is None: return node.val
# 
#         pathsum_left = self.dfs(node.left)
#         pathsum_right = self.dfs(node.right)
# 
#         pathsum_left_disconnected = False
#         if node.left:
#             if node.left.val+pathsum_left < pathsum_left: pathsum_left_disconnected = True
#         complete_sum_left = -math.inf if pathsum_left_disconnected else max(pathsum_left,0) + max(pathsum_right,0) + node.val
# 
#         pathsum_right_disconnected = False
#         if node.right:
#             if node.right.val+pathsum_right < pathsum_right: pathsum_right_disconnected = True
#         complete_sum_right = -math.inf if pathsum_right_disconnected else max(pathsum_left,0) + max(pathsum_right,0) + node.val
#         complete_sum = max(complete_sum_right, complete_sum_left)
#         res = max(pathsum_left, pathsum_right, complete_sum, node.val)
#         
#         
#         return res

"""
get left path sum,
get right path sum
bigges path sum is max(left, right, node)
"""
from collections import deque
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -math.inf
        self.dfs(root)
        return self.max_path
    
    def dfs(self, node):
        if node is None: return 0

        pathsum_left = max(self.dfs(node.left), 0)
        pathsum_right = max(self.dfs(node.right), 0)

        self.max_path = max(self.max_path, pathsum_left + pathsum_right+  node.val)

        return max(pathsum_left + node.val, pathsum_right + node.val )
        
        

