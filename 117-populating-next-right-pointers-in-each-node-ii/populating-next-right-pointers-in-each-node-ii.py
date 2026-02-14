"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
populate, the input is aa node

looks like BFS

# is the end of the level

visit node

the queue for this one is something like¨
[1,2,3,4,5,7]

so the right element is the right element in the queue
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        q.append(root)
        while q:
            current_level = []
            level_size = len(q)
            for element in range(level_size):
                node = q.popleft()
                if node:
                    if len(current_level) >= 1:
                        current_level[len(current_level)-1].next = node
                    current_level.append(node)
                    q.append(node.left)
                    q.append(node.right)
                    
                    
        return root