# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.sequence = deque()
        self.dfs(root)
        print(self.sequence)
    def next(self) -> int:
        current = self.sequence.popleft()
        return current

    def hasNext(self) -> bool:
        return len(self.sequence) > 0
    def dfs(self, root):
        if root is None: return None
        self.dfs(root.left)
        self.sequence.append(root.val)

        self.dfs(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()